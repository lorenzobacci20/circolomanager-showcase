for (const gallery of document.querySelectorAll('[data-gallery]')) {
  const tabs = gallery.querySelector('.tabs');
  const buttons = Array.from(tabs.querySelectorAll('button'));
  const panels = Array.from(gallery.querySelectorAll('.panel'));

  function select(index) {
    buttons.forEach((button, position) => {
      const active = position === index;
      button.setAttribute('aria-selected', String(active));
      button.tabIndex = active ? 0 : -1;
      panels[position].hidden = !active;
    });
  }

  buttons.forEach((button, index) => {
    button.setAttribute('role', 'tab');
    button.setAttribute('aria-controls', panels[index].id);
    panels[index].setAttribute('role', 'tabpanel');
    panels[index].setAttribute('aria-labelledby', button.id);
    button.addEventListener('click', () => select(index));
    button.addEventListener('keydown', (event) => {
      const last = buttons.length - 1;
      const next = {
        ArrowLeft: (index + last) % buttons.length,
        ArrowRight: (index + 1) % buttons.length,
        Home: 0,
        End: last
      }[event.key];
      if (next === undefined) return;
      event.preventDefault();
      select(next);
      buttons[next].focus();
    });
  });

  tabs.setAttribute('role', 'tablist');
  select(0);
  gallery.classList.add('ready');
  tabs.hidden = false;
}
