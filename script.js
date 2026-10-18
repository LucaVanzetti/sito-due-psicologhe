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

const mobileContactBar = document.createElement('aside');
mobileContactBar.className = 'mobile-contact-bar';
mobileContactBar.setAttribute('aria-label', 'Contatti rapidi');
mobileContactBar.innerHTML = `
  <a class="mobile-call" href="tel:+393466519968">
    <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8 10a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.9.6 2.9.7a2 2 0 0 1 1.7 2z"/></svg>
    Chiama
  </a>
  <a class="mobile-write" href="https://wa.me/393669539230" rel="noopener">
    <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.2 9.2 0 0 1-3.9-.9L3 21l1.7-4.6A8 8 0 0 1 3 11.5a8.4 8.4 0 0 1 9-8.4 8.4 8.4 0 0 1 9 8.4z"/><path d="M8 10.2c.3 1.8 2.1 3.6 3.9 3.9M9.3 8.6l-.6 1.1M14.7 14.5l1.1-.6"/></svg>
    Scrivi
  </a>`;
document.body.append(mobileContactBar);
