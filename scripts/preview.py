"""Serve the built showcase on loopback, including seekable video playback."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re

SITE_PATH = "/circolomanager-showcase/"
DIST = Path(__file__).resolve().parents[1] / "dist"


class Preview(SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split("?", 1)[0]
        if path == "/":
            self.send_response(302)
            self.send_header("Location", SITE_PATH)
            self.end_headers()
            return None
        if not path.startswith(SITE_PATH):
            self.send_error(404)
            return None
        self.path = self.path[len(SITE_PATH) - 1:]
        self.bytes_left = None
        if self.path.split("?", 1)[0] != "/assets/media/walkthrough.mp4":
            return super().send_head()

        video = DIST / "assets/media/walkthrough.mp4"
        if not video.is_file():
            self.send_error(404)
            return None
        size = video.stat().st_size
        start, end = 0, size - 1
        requested = self.headers.get("Range")
        if requested is not None:
            match = re.fullmatch(r"bytes=(\d*)-(\d*)", requested)
            if match and any(match.groups()):
                first, last = match.groups()
                start = int(first) if first else max(0, size - int(last))
                end = min(int(last), size - 1) if first and last else size - 1
            if not match or not any(match.groups()) or start > end:
                self.send_response(416)
                self.send_header("Content-Range", f"bytes */{size}")
                self.end_headers()
                return None
        self.bytes_left = end - start + 1
        self.send_response(206 if requested else 200)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Type", "video/mp4")
        self.send_header("Content-Length", str(self.bytes_left))
        if requested:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        stream = video.open("rb")
        stream.seek(start)
        return stream

    def copyfile(self, source, output):
        if self.bytes_left is None:
            return super().copyfile(source, output)
        while self.bytes_left:
            block = source.read(min(65536, self.bytes_left))
            if not block:
                break
            output.write(block)
            self.bytes_left -= len(block)

    def list_directory(self, path):
        self.send_error(404)
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    port = parser.parse_args().port
    if not (DIST / "index.html").is_file():
        parser.exit(1, "Build the site before starting its preview.\n")
    with ThreadingHTTPServer(("127.0.0.1", port), partial(Preview, directory=str(DIST))) as server:
        print(f"http://127.0.0.1:{server.server_port}{SITE_PATH}", flush=True)
        server.serve_forever()
