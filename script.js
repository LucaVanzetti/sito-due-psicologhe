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

if (!document.body.classList.contains('contact-page')) {
  const mobileContactBar = document.createElement('aside');
  mobileContactBar.className = 'mobile-contact-bar';
  mobileContactBar.setAttribute('aria-label', 'Scrivici su WhatsApp');
  mobileContactBar.setAttribute('aria-hidden', 'true');
  mobileContactBar.innerHTML = `
  <a class="mobile-valentina" href="https://wa.me/393669539230" rel="noopener" aria-label="Scrivi a Valentina su WhatsApp">
    <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.2 9.2 0 0 1-3.9-.9L3 21l1.7-4.6A8 8 0 0 1 3 11.5a8.4 8.4 0 0 1 9-8.4 8.4 8.4 0 0 1 9 8.4z"/><path d="M8 10.2c.3 1.8 2.1 3.6 3.9 3.9M9.3 8.6l-.6 1.1M14.7 14.5l1.1-.6"/></svg>
    <span><small>Scrivi a</small>Valentina</span>
  </a>
  <a class="mobile-silvia" href="https://wa.me/393534259158" rel="noopener" aria-label="Scrivi a Silvia su WhatsApp">
    <svg aria-hidden="true" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.2 9.2 0 0 1-3.9-.9L3 21l1.7-4.6A8 8 0 0 1 3 11.5a8.4 8.4 0 0 1 9-8.4 8.4 8.4 0 0 1 9 8.4z"/><path d="M8 10.2c.3 1.8 2.1 3.6 3.9 3.9M9.3 8.6l-.6 1.1M14.7 14.5l1.1-.6"/></svg>
    <span><small>Scrivi a</small>Silvia</span>
  </a>`;
  document.body.append(mobileContactBar);

  const revealPoint = document.querySelector('.hero')?.offsetHeight ?? 300;
  const updateMobileContactBar = () => {
    const isVisible = window.scrollY > revealPoint;
    mobileContactBar.classList.toggle('is-visible', isVisible);
    mobileContactBar.setAttribute('aria-hidden', String(!isVisible));
    mobileContactBar.inert = !isVisible;
  };

  window.addEventListener('scroll', updateMobileContactBar, { passive: true });
  window.addEventListener('resize', updateMobileContactBar);
  updateMobileContactBar();
}
