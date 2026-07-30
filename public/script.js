document.addEventListener('DOMContentLoaded', () => {

  // ─── Header scroll effect ───
  const header = document.querySelector('header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 20);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ─── Copy to Clipboard ───
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const code = btn.nextElementSibling?.innerText || '';
      if (!code) return;
      navigator.clipboard.writeText(code).then(() => {
        const icon = btn.querySelector('i');
        const orig = icon.className;
        icon.className = 'fas fa-check';
        btn.style.color = '#10b981';
        btn.style.borderColor = '#10b981';
        setTimeout(() => {
          icon.className = orig;
          btn.style.color = '';
          btn.style.borderColor = '';
        }, 2000);
      }).catch(() => {});
    });
  });

  // ─── Accordion ───
  document.querySelectorAll('.accordion-header').forEach(h => {
    h.addEventListener('click', () => {
      h.parentElement.classList.toggle('active');
    });
  });

  // ─── Terminal typing stagger ───
  document.querySelectorAll('.terminal-line').forEach((line, i) => {
    line.style.animationDelay = `${0.3 + i * 0.12}s`;
  });

  // ─── Scroll Reveal (Intersection Observer) ───
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.box-reveal').forEach(el => observer.observe(el));

  // ─── Reveal already-visible elements immediately ───
  requestAnimationFrame(() => {
    document.querySelectorAll('.box-reveal:not(.visible)').forEach(el => {
      if (el.getBoundingClientRect().top < window.innerHeight - 60) {
        el.classList.add('visible');
      }
    });
  });
});
