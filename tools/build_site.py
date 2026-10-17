"""Builds the Verbix static site into /mnt/project-files/verbix/website/."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
WA = '920000000000'          # replace with the real WhatsApp number (country code, no +)
WA_SHOW = '+92 000 0000000'  # how it reads on the page
EMAIL = 'hello@verbixacademic.com'
YEAR = '2026'

HL = ('<svg aria-hidden="true" viewBox="0 0 300 60" preserveAspectRatio="none">'
      '<path d="M3 14 C 60 4, 180 2, 297 9 L 294 50 C 210 57, 80 55, 6 49 Z" fill="#F4E04D"/></svg>')
WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.4-.3Z"/></svg>')
TICK = ('<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 10.5 8 15 17 4.5" fill="none" stroke="#1B3FC1" '
        'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h11m-4-5 5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def hl(text):
    return f'<span class="hl">{HL}{text}</span>'


def wa(msg='Hi Verbix, I would like a quote for my document.'):
    return f'https://wa.me/{WA}?text=' + msg.replace(' ', '%20').replace(',', '%2C')


# Free Unsplash photos, hotlinked. To use your own photo instead, put it in
# assets/img/ and change the value here to 'assets/img/<file>.jpg'.
U = 'https://images.unsplash.com/photo-{}?auto=format&fit=crop&w=1200&q=70'
IMG = {
    'students-business': U.format('1522202176988-66273c2fd55f'),
    'students-nursing': U.format('1584432810601-6c7f27d2362b'),
    'students-computing': U.format('1580894908361-967195033215'),
    'students-engineering': U.format('1581092160607-ee22621dd758'),
    'campus-library': U.format('1683319598210-d70486f2f996'),
    'campus-exterior': U.format('1562774053-701939374585'),
    'study-desk': U.format('1450101499163-c8848c66ca85'),
    'editor-portrait': U.format('1635859890085-ec8cb5466806'),
    'students-table': U.format('1517048676732-d65bc937f952'),
    'student-reading': U.format('1529007196863-d07650a3f0ea'),
    'lecture-hall': U.format('1536925155833-43e9c2b2f499'),
    'campus-walk': U.format('1576495199011-eb94736d05d6'),
    'students-cafe': U.format('1543269865-cbf427effbad'),
    'library-shelves': U.format('1427504494785-3a9ca7044f45'),
}


def photo(name, label, alt, extra=''):
    return (f'<div class="photo{extra}"><span>Photo: {label}</span>'
            f'<img src="{IMG[name]}" alt="{alt}" loading="lazy" onerror="this.remove()"></div>')


NAV = [('index.html', 'Home'), ('services.html', 'Services'), ('pricing.html', 'Pricing'),
       ('about.html', 'About'), ('faq.html', 'FAQ'), ('samples.html', 'Free sample')]


def page(fname, title, desc, body, cta=True):
    links = ''.join(
        ('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == fname else '', t)) for h, t in NAV)
    cta_html = f'''
<section class="cta band-night">
  <div class="wrap">
    <div class="copy rv">
      <h2>Not sure yet? Try us first.</h2>
      <p>Before you trust us with your work, ask for a free sample. Tell us your subject and we will send real tracked edits, so you can judge the quality before you pay anything.</p>
    </div>
    <div class="actions rv">
      <a class="btn btn-yellow" href="{wa('Hi Verbix, could I see a sample edit for my subject?')}">{WA_ICON}Ask for a free sample</a>
      <a class="btn btn-text" style="color:#fff" href="samples.html">How samples work</a>
    </div>
  </div>
</section>''' if cta else ''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#1B3FC1">
<link rel="icon" href="assets/logo/mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;700;800;900&amp;family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&amp;display=swap">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Verbix home"><img src="assets/logo/wordmark-primary.svg" alt="Verbix" width="128" height="30"></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn btn-blue" href="contact.html">Get a quote</a></nav>
  </div>
</header>
<main id="main">
{body}
{cta_html}
</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="brand" style="display:flex;flex-direction:column;gap:16px">
      <img src="assets/logo/wordmark-reverse.svg" alt="Verbix" width="128" height="30" style="height:30px;width:auto;align-self:flex-start">
      <p style="max-width:22em">Academic editing, feedback and guidance for students and researchers. Your ideas, your words, made clearer.</p>
    </div>
    <div><h3>Services</h3><ul>
      <li><a href="services.html#language">Proofreading and editing</a></li>
      <li><a href="services.html#structure">Thesis and dissertation</a></li>
      <li><a href="services.html#format">Citations and formatting</a></li>
      <li><a href="services.html#technical">Code, slides and surveys</a></li>
    </ul></div>
    <div><h3>Verbix</h3><ul>
      <li><a href="about.html">About us</a></li>
      <li><a href="pricing.html">Pricing</a></li>
      <li><a href="faq.html">FAQ</a></li>
      <li><a href="samples.html">Free sample</a></li>
      <li><a href="integrity.html">Our standards</a></li>
    </ul></div>
    <div><h3>Talk to us</h3><ul>
      <li><a href="{wa()}">WhatsApp {WA_SHOW}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="contact.html">Quote form</a></li>
    </ul></div>
    <div class="legal"><span>&copy; {YEAR} Verbix. Editing and guidance only. We never write assignments for you.</span><span><a href="integrity.html">Academic integrity policy</a></span></div>
  </div>
</footer>
<a class="wa-float" href="{wa()}" aria-label="Chat with Verbix on WhatsApp" style="color:#fff">{WA_ICON}</a>
<script src="assets/js/site.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), 'w') as f:
        f.write(html)


# ---------------------------------------------------------------- Home
FIELDS = [
    ('students-business', 'business students', 'Business students discussing a report', 'Business and management',
     'Case studies, reports and MBA dissertations that read like a professional wrote them.'),
    ('students-nursing', 'nursing students', 'A nursing student with a stethoscope', 'Nursing and health',
     'Reflective essays, care plans and literature reviews with every reference in order.'),
    ('students-computing', 'computing students', 'A computing student working at a computer', 'Computing and IT',
     'Technical reports and project write-ups, plus a review of your Java, Python or C++ code.'),
    ('students-engineering', 'engineering students', 'An engineering student operating machinery in a workshop', 'Engineering and science',
     'Lab reports and theses where the method is clear and the results are easy to follow.'),
]
fields_html = ''.join(
    f'<div class="field rv">{photo(n, l, a)}<h3>{t}</h3><p>{p}</p></div>' for n, l, a, t, p in FIELDS)

home = f'''
<section class="manuscript">
  <div class="wrap">
    <div class="ms-main">
      <p class="kicker">Academic editing and feedback</p>
      <h1>Hand in work <span class="del">that</span> you&rsquo;re {hl('proud of.')}</h1>
      <p class="lead">An experienced academic editor reads your essay, dissertation or report line by line. You keep your ideas and your voice. We make sure every sentence says what you meant.</p>
      <div class="actions">
        <a class="btn btn-blue" href="{wa()}">{WA_ICON}Get a quote on WhatsApp</a>
        <a class="btn btn-text" href="pricing.html">See prices</a>
      </div>
      <p class="muted" style="font-size:1rem">Your quote arrives within 2 hours. Not ready to commit? <a href="samples.html">Ask for a free sample first.</a></p>
    </div>
    <aside class="ms-margin" aria-label="Example editor notes">
      <p class="label">In the margin</p>
      <div class="note edit tie"><div class="who"><span>Deleted: &ldquo;that&rdquo;</span><span>Editor</span></div><p>Shorter reads stronger. The sentence works without it.</p></div>
      <div class="note comment"><div class="who"><span>Comment</span><span>Editor</span></div><p>Good word choice. Keep &ldquo;proud&rdquo;, it is honest and it is yours.</p></div>
      <div class="note"><div class="who"><span>Formatted</span><span>Editor</span></div><p>APA 7, Harvard, MLA or Chicago. References checked against your list.</p></div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div style="display:flex;flex-direction:column;gap:14px"><p class="kicker">Who we help</p><h2>Every field has its own rules.<br>We know them.</h2></div>
      <p>From a first-year essay to a PhD chapter, we edit for the conventions your department marks against.</p>
    </div>
    <div class="fields">{fields_html}</div>
  </div>
</section>

<section class="section band-blue">
  <div class="wrap">
    <div class="section-head">
      <div style="display:flex;flex-direction:column;gap:14px"><p class="kicker" style="color:var(--highlighter)">How it works</p><h2>Four steps. No surprises.</h2></div>
    </div>
    <ol class="steps">
      <li class="rv"><span class="n">1</span><h3>Send your draft</h3><p>On WhatsApp or by email. Add the brief or marking rubric if you have one.</p></li>
      <li class="rv"><span class="n">2</span><h3>Get a clear quote</h3><p>A fixed price and a delivery date within 2 hours. Pay only when you agree.</p></li>
      <li class="rv"><span class="n">3</span><h3>We edit, line by line</h3><p>Every change is tracked in Word or Google Docs, with comments that explain why.</p></li>
      <li class="rv"><span class="n">4</span><h3>You decide</h3><p>Accept or reject each change. Questions afterwards are free for 7 days.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap about-grid">
    {photo('lecture-hall', 'student reading in a lecture hall', 'A student reading alone in an empty lecture hall')}
    <div class="prose rv">
      <p class="kicker">Free sample</p>
      <h2 style="margin-top:0;font-size:clamp(2.1rem,4vw,3.2rem)">See our editing before you trust us with yours.</h2>
      <p>Handing your work to someone new takes trust, so you don&rsquo;t have to take our word for it. Tell us your subject and level, and we will send you a free sample of real tracked edits in that field.</p>
      <ul>
        <li>Free, with no obligation to order</li>
        <li>Matched to your subject: business, nursing, computing, engineering and more</li>
        <li>Usually sent the same day on WhatsApp or email</li>
      </ul>
      <div class="actions"><a class="btn btn-blue" href="{wa('Hi Verbix, could I see a free sample edit for my subject?')}">{WA_ICON}Ask for a free sample</a><a class="btn btn-text" href="samples.html">How it works</a></div>
    </div>
  </div>
</section>

<section class="section band-margin">
  <div class="wrap split">
    <div class="rv">
      <p class="kicker">Services and prices</p>
      <h2>Pick what your draft needs.</h2>
      <p class="muted">Prices are per 1,000 words with standard 5-day delivery. Faster delivery is available.</p>
      <div class="actions"><a class="btn btn-line" href="services.html">All 13 services {ARROW}</a></div>
    </div>
    <div class="index rv">
      <a href="services.html#language"><span class="name">Proofreading</span><span class="dots"></span><span class="price">from $10</span></a>
      <a href="services.html#language"><span class="name">Academic editing</span><span class="tag">Most chosen</span><span class="dots"></span><span class="price">from $18</span></a>
      <a href="services.html#structure"><span class="name">Editing with argument feedback</span><span class="dots"></span><span class="price">from $28</span></a>
      <a href="services.html#structure"><span class="name">Thesis and dissertation support</span><span class="dots"></span><span class="price">per chapter</span></a>
      <a href="services.html#format"><span class="name">Citations, formatting, slides, surveys, code review</span><span class="dots"></span><span class="price">ask us</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap about-grid">
    {photo('campus-library', 'university library', 'Students studying in a university library')}
    <div class="prose rv">
      <p class="kicker">Why Verbix</p>
      <h2 style="margin-top:0;font-size:clamp(2.1rem,4vw,3.2rem)">Six years of marking-grade reading, in your corner.</h2>
      <p>Verbix is run by an academic writing specialist with six years of experience across business, health, computing and the social sciences. You deal with the editor directly, not a call centre.</p>
      <ul>
        <li>One named editor for your whole project</li>
        <li>Your file is never shared, sold or reused</li>
        <li>Editing and guidance only, never ghostwriting</li>
      </ul>
      <div class="actions"><a class="btn btn-text" href="about.html">Meet the editor</a><a class="btn btn-text" href="integrity.html">Read our standards</a></div>
    </div>
  </div>
</section>
'''
page('index.html', 'Verbix | Academic editing, proofreading and feedback',
     'Academic proofreading, editing and feedback for essays, dissertations and reports. Quote within 2 hours on WhatsApp.', home)

# ---------------------------------------------------------------- Services
GROUPS = [
    ('language', 'Language and clarity', 'For drafts where the ideas are there and the English needs to catch up.', [
        ('Proofreading', 'Spelling, grammar, punctuation and consistency. The final check before you submit.',
         [('Best for', 'Finished drafts'), ('From', '$10 per 1,000 words')]),
        ('Academic editing', 'Everything in proofreading, plus clearer sentences, better flow and a consistent academic tone.',
         [('Best for', 'Most essays and reports'), ('From', '$18 per 1,000 words')]),
        ('English language support', 'Patient editing for writers whose first language is not English, with notes that help you improve next time.',
         [('Best for', 'International students'), ('From', '$18 per 1,000 words')]),
        ('Assignment, report and case study editing', 'Editing tuned to the brief: word count, structure and the marking criteria you were given.',
         [('Best for', 'Coursework'), ('From', '$18 per 1,000 words')]),
    ]),
    ('structure', 'Structure and argument', 'For work that needs a second reader who thinks like an examiner.', [
        ('Structure and argument feedback', 'A written report on how your argument holds together, where it is weak and what to move.',
         [('Best for', 'Drafts that feel messy'), ('From', '$28 per 1,000 words')]),
        ('Thesis and dissertation support', 'Chapter-by-chapter editing and feedback across the whole project, with one editor from start to finish.',
         [('Best for', 'Masters and PhD'), ('From', '$250 per chapter')]),
        ('Research proposal and literature review guidance', 'Feedback on your research question, scope, sources and how your review builds a case.',
         [('Best for', 'Proposals'), ('From', 'Quote on request')]),
    ]),
    ('format', 'Citations and formatting', 'For the details that lose easy marks.', [
        ('Citation and referencing support', 'We check every in-text citation against your reference list in APA, MLA, Harvard or Chicago.',
         [('Styles', 'APA, MLA, Harvard, Chicago'), ('From', 'Included in editing, or $8 per 1,000 words')]),
        ('Formatting service', 'Headings, margins, contents page, figures and tables set to your university template.',
         [('Best for', 'Theses and long reports'), ('From', 'Quote on request')]),
        ('Similarity report review', 'We read your Turnitin or similar report with you and show where quoting, paraphrasing or citing needs fixing.',
         [('Best for', 'Understanding a report'), ('From', '$15 per report')]),
    ]),
    ('technical', 'Technical and presentation', 'For the parts of a project that are not an essay.', [
        ('Code review', 'Readability, structure and comments reviewed for Java, Python and C++ coursework code.',
         [('Languages', 'Java, Python, C++'), ('From', '$30 per 300 lines')]),
        ('Presentation design support', 'Your content laid out as clean, readable slides in PowerPoint or Google Slides.',
         [('Best for', 'Seminars and vivas'), ('From', '$8 per slide, $40 minimum')]),
        ('Survey and Google Forms setup', 'Your questionnaire built as a tidy, tested Google Form with clear wording and logic.',
         [('Best for', 'Research data collection'), ('From', '$30 per form')]),
    ]),
]


def svc(t, p, dl):
    rows = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in dl)
    return (f'<article class="svc rv"><h3>{t}</h3><p>{p}</p><dl>{rows}</dl>'
            f'<a class="get" href="{wa("Hi Verbix, I would like a quote for " + t.lower() + ".")}">Get a quote {ARROW}</a></article>')


groups_html = ''.join(
    f'<div class="group" id="{gid}"><div><p class="kicker">0{i + 1}</p><h2 style="font-size:clamp(1.8rem,3vw,2.4rem)">{gt}</h2><p class="muted">{gp}</p></div>'
    f'<div class="svc-list">{"".join(svc(*s) for s in items)}</div></div>'
    for i, (gid, gt, gp, items) in enumerate(GROUPS))

services = f'''
<section class="page-head">
  <div class="wrap">
    <div class="copy">
      <p class="kicker">Services</p>
      <h1>Thirteen ways to make your draft {hl('clearer.')}</h1>
      <p class="lead">Not sure which one you need? Send the draft and the brief. We will recommend the lightest service that does the job.</p>
    </div>
    {photo('study-desk', 'student editing a draft', 'A student reviewing printed pages with a pen')}
  </div>
</section>
<section class="section"><div class="wrap">{groups_html}</div></section>
'''
page('services.html', 'Services | Verbix academic editing',
     'Proofreading, academic editing, argument feedback, thesis support, citations, formatting, code review and more.', services)

# ---------------------------------------------------------------- Pricing
def plan(name, price, unit, who, items, pick=False):
    lis = ''.join(f'<li>{TICK}<span>{x}</span></li>' for x in items)
    tag = '<span class="tag" style="align-self:flex-start">Most chosen</span>' if pick else ''
    btn = 'btn-blue' if pick else 'btn-line'
    return (f'<div class="plan{" pick" if pick else ""} rv">{tag}<h3>{name}</h3><p class="muted" style="font-size:1rem">{who}</p>'
            f'<p class="price">{price} <small>{unit}</small></p><ul>{lis}</ul>'
            f'<a class="btn {btn}" href="{wa("Hi Verbix, I would like a quote for " + name + ".")}">Get a quote</a></div>')


plans = ''.join([
    plan('Proofread', '$10', 'per 1,000 words', 'Your final check before submitting.',
         ['Spelling, grammar and punctuation', 'Consistent spelling and style', 'Tracked changes in Word or Google Docs', '5-day delivery']),
    plan('Edit', '$18', 'per 1,000 words', 'Clearer sentences and a confident academic tone.',
         ['Everything in Proofread', 'Clarity, flow and word choice', 'Citation check in your style', 'Margin comments that explain why'], pick=True),
    plan('Edit + Feedback', '$28', 'per 1,000 words', 'For drafts that need an examiner’s eye.',
         ['Everything in Edit', 'Written report on structure and argument', 'Checked against your brief or rubric', 'One follow-up question round']),
    plan('Thesis Partner', '$250', 'per chapter', 'One editor for your whole thesis or dissertation.',
         ['Chapters up to 8,000 words', 'Edit + Feedback on every chapter', 'Consistency across the full document', 'Full dissertation from $1,200']),
])

ADDONS = [
    ('Survey and Google Forms setup', '$30 per form', 'Built, tested and shared with you'),
    ('Presentation slides', '$8 per slide', '$40 minimum'),
    ('Code review', '$30 per 300 lines', 'Java, Python or C++'),
    ('Similarity report review', '$15 per report', 'Turnitin or similar'),
    ('Formatting to a template', 'Quote on request', 'Depends on length and template'),
    ('Delivery in 48 hours', '+50%', 'On any language service'),
    ('Delivery in 24 hours', '+100%', 'Subject to availability'),
]
rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td class="muted">{c}</td></tr>' for a, b, c in ADDONS)

pricing = f'''
<section class="page-head">
  <div class="wrap">
    <div class="copy">
      <p class="kicker">Pricing</p>
      <h1>A fixed price, {hl('before')} you pay.</h1>
      <p class="lead">Send your file and you will get an exact quote within 2 hours. No hidden fees and no payment until you say yes.</p>
    </div>
    {photo('students-table', 'students working together', 'Students working through papers together at a table')}
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="plans">{plans}</div>
    <p class="muted" style="margin-top:28px;font-size:1rem">Prices in US dollars. Minimum order $15. Prices in Pakistani rupees are available on request.</p>
  </div>
</section>
<section class="section band-margin">
  <div class="wrap split">
    <div class="rv">
      <p class="kicker">Extras</p>
      <h2>Add-ons and faster delivery</h2>
      <p class="muted">Order on their own or add to any plan.</p>
    </div>
    <div class="table-box rv">
      <table class="addons"><thead><tr><th>Service</th><th>Price</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="note comment rv" style="max-width:760px;padding:28px 30px">
      <div class="who"><span>Launch offer</span><span>Limited</span></div>
      <p style="font-size:1.2rem">Our first 50 clients get 20% off their first order. Mention it when you ask for your quote.</p>
    </div>
  </div>
</section>
'''
page('pricing.html', 'Pricing | Verbix academic editing',
     'Proofreading from $10, editing from $18 and feedback from $28 per 1,000 words. Fixed quote within 2 hours.', pricing)

# ---------------------------------------------------------------- About
about = f'''
<section class="page-head">
  <div class="wrap">
    <div class="copy">
      <p class="kicker">About Verbix</p>
      <h1>The second reader every {hl('draft')} deserves.</h1>
      <p class="lead">Verbix started with one belief: students deserve feedback that teaches, not just corrections that disappear.</p>
    </div>
    {photo('campus-exterior', 'university campus', 'A university campus building')}
  </div>
</section>
<section class="section">
  <div class="wrap about-grid">
    {photo('editor-portrait', 'editor at work', 'An editor working through a stack of printed pages')}
    <div class="prose rv">
      <p class="kicker">The editor</p>
      <h2 style="margin-top:0">Six years in academic writing</h2>
      <p>Our founder has spent six years helping students and researchers present their work clearly, across business, nursing, computing, engineering and the social sciences.</p>
      <p>That experience means knowing what markers look for: a clear argument, evidence used well, consistent referencing and English that never gets in the way of the ideas.</p>
      <p>Every Verbix order is handled personally. You will know who is reading your work, and you can ask them questions directly.</p>
      <h2>What we will never do</h2>
      <p>We do not write assignments, take exams or produce work for you to submit as your own. Your ideas and arguments stay yours. Read <a href="integrity.html">our standards</a> for the full policy.</p>
    </div>
  </div>
</section>
<section class="section band-margin">
  <div class="wrap">
    <div class="section-head"><h2>What you can count on</h2></div>
    <div class="values">
      <div class="rv"><h3>Your voice stays</h3><p>We edit to make you sound like the best version of yourself, not like us.</p></div>
      <div class="rv"><h3>Every change explained</h3><p>Tracked changes and margin comments, so you learn as well as improve.</p></div>
      <div class="rv"><h3>Private by default</h3><p>Files are used only for your order and deleted on request.</p></div>
      <div class="rv"><h3>Straight answers</h3><p>A real person replies on WhatsApp or email, usually within 2 hours.</p></div>
    </div>
  </div>
</section>
'''
page('about.html', 'About | Verbix academic editing',
     'Verbix is led by an academic writing specialist with six years of experience. Editing and guidance, never ghostwriting.', about)

# ---------------------------------------------------------------- FAQ
FAQ = [
    ('Is using an editor allowed by my university?',
     ['Most universities allow proofreading and editing that does not change your ideas or arguments. Some set limits, so check your handbook. Our editing is designed to stay within the usual university guidelines for third-party proofreading.']),
    ('Will you write my essay or assignment?',
     ['No. We edit and give feedback on work you have written. We do not write new content for you to submit. See <a href="integrity.html">our standards</a>.']),
    ('How do I get a quote?',
     [f'Send your file on <a href="{wa()}">WhatsApp</a> or to <a href="mailto:{EMAIL}">{EMAIL}</a>, with your deadline and the service you want. You will get a fixed price and delivery date within 2 hours.']),
    ('Can I see a sample of your editing?',
     ['Yes, and it is free. Tell us your subject and level, and we will send a short excerpt of real tracked edits in that field, so you can judge our work before you trust us with yours. We do not publish samples online to protect our clients’ work. <a href="samples.html">How samples work</a>.']),
    ('How do I pay?',
     ['Once you accept the quote, we send the payment options with it. You pay before the edit starts, and the price never changes after you agree.']),
    ('What do I get back?',
     ['Your document with every change tracked, margin comments explaining important edits, and a clean copy with all changes accepted. Feedback plans also include a short written report.']),
    ('How fast can you deliver?',
     ['Standard delivery is 5 days. 48-hour delivery costs 50% more and 24-hour delivery costs double, subject to availability.']),
    ('Is my work kept private?',
     ['Yes. Your file is only used for your order. We never share, sell or reuse it, and we delete it on request.']),
    ('Which referencing styles do you know?',
     ['APA 7, MLA, Harvard and Chicago, plus most university variations of Harvard. Send your style guide if your department has one.']),
    ('What if I am not happy with the edit?',
     ['Tell us within 7 days. We will review the parts you are unsure about and revise them at no cost.']),
]
faq_html = ''.join(
    f'<details class="rv"><summary>{q}</summary><div>{"".join(f"<p>{a}</p>" for a in ans)}</div></details>' for q, ans in FAQ)
faq = f'''
<section class="page-head">
  <div class="wrap"><div class="copy">
    <p class="kicker">FAQ</p>
    <h1>Good {hl('questions.')}</h1>
    <p class="lead">The things students ask us most. Anything else, ask on WhatsApp.</p>
  </div>
  {photo('students-cafe', 'students talking', 'A group of students talking at a cafe table')}
  </div>
</section>
<section class="section"><div class="wrap"><div class="faq" style="max-width:920px">{faq_html}</div></div></section>
'''
page('faq.html', 'FAQ | Verbix academic editing',
     'Answers about quotes, payment, delivery, samples, privacy and academic integrity.', faq)

# ---------------------------------------------------------------- Integrity
integrity = f'''
<section class="page-head">
  <div class="wrap"><div class="copy">
    <p class="kicker">Our standards</p>
    <h1>Your work stays {hl('yours.')}</h1>
    <p class="lead">Verbix provides editing, feedback and guidance. This page sets out exactly what that means.</p>
  </div>
  {photo('student-reading', 'student with a book', 'A student holding a book in a library')}
  </div>
</section>
<section class="section">
  <div class="wrap policy">
    <div class="do-dont rv">
      <div class="yes"><h3>We do</h3><ul>
        <li>Correct grammar, spelling and punctuation</li>
        <li>Improve clarity, flow and academic tone</li>
        <li>Comment on structure and argument</li>
        <li>Check citations and formatting</li>
        <li>Explain our changes so you can learn</li>
      </ul></div>
      <div class="no"><h3>We don&rsquo;t</h3><ul>
        <li>Write essays, assignments or chapters</li>
        <li>Add new ideas, arguments or research</li>
        <li>Take exams or online tests</li>
        <li>Help hide copied work from similarity checks</li>
        <li>Share your files with anyone</li>
      </ul></div>
    </div>
    <h2>Following your university&rsquo;s rules</h2>
    <p>Many universities publish guidance on proofreading by a third party. Our editing is designed to stay within those limits. If your institution restricts editing, tell us and we will work within that, or tell you honestly if we cannot help.</p>
    <h2>Similarity reports</h2>
    <p>When we review a similarity report, we show you where quotes need marks, paraphrases need rewording in your own words, and sources need citing. The goal is honest, correctly referenced work.</p>
    <h2>Privacy</h2>
    <p>Files are stored only as long as your order needs them and deleted on request. We never use client work as samples. The excerpts we send on request come from consented or self-produced material.</p>
    <h2>Questions</h2>
    <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> and the editor will reply personally.</p>
  </div>
</section>
'''
page('integrity.html', 'Our standards | Verbix academic editing',
     'Verbix offers editing, feedback and guidance only. Read what we do, what we never do and how we protect your privacy.', integrity)


# ---------------------------------------------------------------- Samples
sample_fields = ''.join(
    f'<div class="field rv">{photo(n, l, a)}<h3>{t}</h3></div>' for n, l, a, t, p in FIELDS)
samples = f'''
<section class="page-head">
  <div class="wrap">
    <div class="copy">
      <p class="kicker">Free sample</p>
      <h1>Try us before you {hl('trust us.')}</h1>
      <p class="lead">You should see how we edit before you hand over your work. Ask for a free sample and judge the quality for yourself. No payment, no obligation.</p>
      <div class="actions">
        <a class="btn btn-blue" href="{wa('Hi Verbix, could I see a free sample edit for my subject?')}">{WA_ICON}Ask on WhatsApp</a>
        <a class="btn btn-line" href="mailto:{EMAIL}?subject=Free%20sample%20request">Ask by email</a>
      </div>
    </div>
    {photo('library-shelves', 'student in a university library', 'A student with a backpack beside library bookshelves')}
  </div>
</section>

<section class="section band-blue">
  <div class="wrap">
    <div class="section-head">
      <div style="display:flex;flex-direction:column;gap:14px"><p class="kicker" style="color:var(--highlighter)">How it works</p><h2>Three steps to your sample</h2></div>
    </div>
    <ol class="steps">
      <li class="rv"><span class="n">1</span><h3>Tell us your subject</h3><p>Message us with your subject, level and the service you are thinking about.</p></li>
      <li class="rv"><span class="n">2</span><h3>Get real tracked edits</h3><p>We send a short excerpt in your field, with every change and comment visible.</p></li>
      <li class="rv"><span class="n">3</span><h3>Decide in your own time</h3><p>Order only if you like what you see. No pressure and no follow-up spam.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <div style="display:flex;flex-direction:column;gap:14px"><p class="kicker">Samples by field</p><h2>A sample from your subject, not a generic one.</h2></div>
      <p>We match the sample to your field, so you see how we handle the terms, structure and referencing your markers expect.</p>
    </div>
    <div class="fields">{sample_fields}</div>
  </div>
</section>

<section class="section band-margin">
  <div class="wrap">
    <div class="do-dont rv" style="max-width:980px">
      <div class="yes"><h3>What you get</h3><ul>
        <li>A short excerpt, about one page, with tracked changes</li>
        <li>Margin comments that explain the edits</li>
        <li>A sample from your subject and level</li>
        <li>Free, usually sent the same day</li>
      </ul></div>
      <div class="no"><h3>What a sample is not</h3><ul>
        <li>A finished essay or assignment</li>
        <li>Another client&rsquo;s work. Samples come from material we have permission to use</li>
        <li>A promise of a grade</li>
      </ul></div>
    </div>
  </div>
</section>
'''
page('samples.html', 'Free sample | Verbix academic editing',
     'Ask for a free sample of our editing in your subject before you order. No payment, no obligation.', samples, cta=False)

# ---------------------------------------------------------------- Contact
opts = ''.join(f'<option>{s[0]}</option>' for g in GROUPS for s in g[3])
contact = f'''
<section class="page-head">
  <div class="wrap"><div class="copy">
    <p class="kicker">Contact</p>
    <h1>Send your draft. Get a {hl('quote.')}</h1>
    <p class="lead">A fixed price and delivery date within 2 hours. You pay only when you agree. Want to see our work first? <a href="samples.html">Ask for a free sample.</a></p>
  </div>
  {photo('campus-walk', 'university campus', 'Students walking past a university building')}
  </div>
</section>
<section class="section">
  <div class="wrap" style="display:flex;flex-direction:column;gap:64px">
    <div class="contact-grid">
      <div class="channel wa rv">
        <p class="kicker" style="color:var(--highlighter)">Fastest</p>
        <p class="big">WhatsApp {WA_SHOW}</p>
        <p>Send the file, your deadline and the service you want. Most replies arrive within 2 hours.</p>
        <div class="actions"><a class="btn btn-yellow" href="{wa()}">{WA_ICON}Open WhatsApp</a></div>
      </div>
      <div class="channel mail rv">
        <p class="kicker">Email</p>
        <p class="big">{EMAIL}</p>
        <p class="muted">Best for long documents, theses and anything with several files.</p>
        <div class="actions"><a class="btn btn-line" href="mailto:{EMAIL}">Write an email</a></div>
      </div>
    </div>
    <div class="split">
      <div class="rv">
        <h2>Or use the form</h2>
        <p class="muted">Fill this in and we will turn it into a ready-to-send message. Attach your file in WhatsApp or email.</p>
      </div>
      <form class="quote rv" id="quote-form" data-wa="{WA}" data-email="{EMAIL}">
        <label>Your name<input id="q-name" name="name" autocomplete="name" required></label>
        <label>Email or WhatsApp<input id="q-contact" name="contact" required></label>
        <label>Service<select id="q-service" name="service">{opts}<option>Not sure yet</option></select></label>
        <label>Word count<input id="q-words" name="words" inputmode="numeric" placeholder="e.g. 3,000"></label>
        <label>Deadline<input id="q-deadline" name="deadline" type="date"></label>
        <label>Referencing style<select id="q-style" name="style"><option>APA 7</option><option>Harvard</option><option>MLA</option><option>Chicago</option><option>Other or not sure</option></select></label>
        <label class="full">Anything we should know?<textarea id="q-notes" name="notes" placeholder="Subject, level, and what feedback you have had so far"></textarea><span class="hint">We reply within 2 hours with a fixed price.</span></label>
        <div class="full"><button class="btn btn-blue" type="submit" style="border:0;cursor:pointer">Request my quote</button></div>
      </form>
    </div>
  </div>
</section>
'''
page('contact.html', 'Contact | Verbix academic editing',
     'Send your draft on WhatsApp or email and get a fixed quote within 2 hours.', contact, cta=False)

# ---------------------------------------------------------------- 404
nf = f'''
<section class="page-head" style="border:0">
  <div class="wrap"><div class="copy" style="padding-bottom:80px">
    <p class="kicker">Page not found</p>
    <h1>This page has been <span class="del">deleted</span> {hl('moved.')}</h1>
    <p class="lead">The link may be old. Try the home page, or message us and we will point you to the right place.</p>
    <div class="actions"><a class="btn btn-blue" href="index.html">Go to the home page</a><a class="btn btn-text" href="contact.html">Contact us</a></div>
  </div></div>
</section>
'''
page('404.html', 'Page not found | Verbix', 'This page could not be found.', nf, cta=False)

# ---------------------------------------------------------------- JS
os.makedirs(os.path.join(OUT, 'assets/js'), exist_ok=True)
with open(os.path.join(OUT, 'assets/js/site.js'), 'w') as f:
    f.write('''// Mobile menu
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
''')
with open(os.path.join(OUT, '.nojekyll'), 'w') as f:
    f.write('')
print('built')
