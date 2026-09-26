const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#primary-navigation');

if (toggle && nav) {
  const setMenuState = (isOpen) => {
    nav.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'Chiudi il menu' : 'Apri il menu');
  };

  toggle.addEventListener('click', () => {
    setMenuState(!nav.classList.contains('open'));
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      setMenuState(false);
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav.classList.contains('open')) {
      setMenuState(false);
      toggle.focus();
    }
  });
}
