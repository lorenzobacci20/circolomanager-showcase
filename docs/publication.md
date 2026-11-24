# Publishing the portfolio

The static package is intended as an informational portfolio. Its pages describe the engineering work and show recordings from a fictional club. GitHub Pages restricts sites primarily directed at commercial transactions or commercial SaaS. If the purpose changes to sales, subscriptions or an interactive service, choose hosting whose terms support that use before changing the site. [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) · [Additional product terms](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features)

## Preview a reviewed revision

From a clean checkout of the showcase, run the following commands with Python 3 and Git installed. Open the local address printed by the server. The build needs no package registry, API keys or internet access.

```sh
python3 scripts/build.py --verify-tree
python3 scripts/preview.py
```

`release-files.txt` is the exact reviewed repository inventory. Only the files listed under `site/` enter the static artifact. Source maps, private notes and captures awaiting review belong outside this repository.

## First publication

1. Obtain the owner's explicit approval for the full commit that will become public. Review the entire Git history, repository metadata and media at that revision. Record the approved commit.
2. In the settings of **lorenzobacci20/circolomanager-showcase**, change this showcase repository to public. Under **Pages → Build and deployment → Source**, select **GitHub Actions**.
3. Under **Actions → Publish portfolio → Run workflow**, select `main` and paste the full approved commit into `approved_commit`. The workflow requires a public repository and checks the dispatch revision against that value.
4. Check both jobs and the deployment URL reported in the **github-pages** environment. The expected address is [the portfolio project site](https://lorenzobacci20.github.io/circolomanager-showcase/). Open the English and Italian pages and both versions of the case study in a signed-out browser. Check the walkthrough, language switch, image loading, LinkedIn destination and social image.
5. Record the commit, deployment run, observed URL, time and smoke results. If a smoke check fails, report the observed issue. To restore a previously approved version, revert the change on `main`, review the resulting commit, and dispatch that exact revision.

Changes to `main` alone do not trigger publication. The build output can also be served from a conventional static host. Before changing the public URL, update the canonical links, language alternates, Open Graph URLs and README together.
