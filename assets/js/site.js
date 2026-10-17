// Mobile menu
const btn = document.querySelector('.menu-btn');
const nav = document.getElementById('nav');
if (btn && nav) {
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
    btn.textContent = open ? 'Close' : 'Menu';
  });
}

// Quote form: builds a ready-to-send WhatsApp or email message
const form = document.getElementById('quote-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const d = new FormData(form);
    const lines = [
      'Hi Verbix, I would like a quote.',
      'Name: ' + d.get('name'),
      'Contact: ' + d.get('contact'),
      'Service: ' + d.get('service'),
      'Word count: ' + (d.get('words') || 'not sure'),
      'Deadline: ' + (d.get('deadline') || 'flexible'),
      'Referencing style: ' + d.get('style'),
    ];
    if (d.get('notes')) lines.push('Notes: ' + d.get('notes'));
    const text = lines.join(String.fromCharCode(10));
    const msg = encodeURIComponent(text);
    let box = form.querySelector('.sent');
    if (!box) { box = document.createElement('div'); box.className = 'sent'; form.appendChild(box); }
    box.innerHTML = '<h3>Your message is ready</h3><pre></pre><div class="actions">'
      + '<a class="btn btn-blue" href="https://wa.me/' + form.dataset.wa + '?text=' + msg + '">Send on WhatsApp</a>'
      + '<a class="btn btn-line" href="mailto:' + form.dataset.email + '?subject=Quote%20request&body=' + msg + '">Send by email</a></div>'
      + '<p class="hint">Attach your document after the message opens. We reply within 2 hours with a fixed price.</p>';
    box.querySelector('pre').textContent = text;
    box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  });
}
