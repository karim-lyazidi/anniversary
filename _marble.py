import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ──────────────────────────────────────────────
# 1. REPLACE CSS VARIABLES PALETTE
# ──────────────────────────────────────────────
old_vars = r""":root {
    --cream: #fdfaf6;
    --cream-dark: #f8f1e8;
    --paper: #f4ece1;
    --paper-dark: #ebe1d3;
    --beige: #f7f1e3;
    --champagne: #f0e6d2;
    --dusty-pink: #c98a8a;
    --dusty-pink-deep: #a66868;
    --dusty-pink-soft: #e8caca;
    --blush: #f4d9d4;
    --gold: #c9a86c;
    --gold-soft: #e6d3a3;
    --gold-deep: #b8944a;
    --ink: #3e2d28;
    --ink-soft: #5c4540;
    --ink-faint: #8b756f;
    --shadow-soft: rgba(62, 45, 40, 0.08);
    --shadow-medium: rgba(62, 45, 40, 0.14);
    --shadow-deep: rgba(62, 45, 40, 0.22);
    --tape: rgba(212, 184, 138, 0.42);
    --tape-pink: rgba(201, 138, 138, 0.28);
}"""

new_vars = r""":root {
    --marble-white: #ffffff;
    --marble-ice: #f9fafb;
    --marble-snow: #f5f7fa;
    --marble-cloud: #eef1f6;
    --marble-vein: #d4cfc5;
    --marble-vein-deep: #b8ad9e;
    --marble-shadow: #c5cbd6;
    --gold: #c9a86c;
    --gold-soft: #e6d3a3;
    --gold-deep: #b8944a;
    --gold-bright: #d4b36d;
    --gold-champagne: #e9d9b4;
    --gold-light: #f3e6c4;
    --ink: #2c2a28;
    --ink-soft: #4a4743;
    --ink-faint: #7b7770;
    --shadow-soft: rgba(50, 45, 35, 0.06);
    --shadow-medium: rgba(50, 45, 35, 0.12);
    --shadow-deep: rgba(50, 45, 35, 0.20);
    --shadow-gold: rgba(201, 168, 108, 0.18);
}"""

content = content.replace(old_vars, new_vars)

# ──────────────────────────────────────────────
# 2. META THEME COLOR & BODY BACKGROUND
# ──────────────────────────────────────────────
content = content.replace('#fdfaf6', '#f9fafb')

old_body_bg = """html, body {
    width: 100%;
    height: 100%;
    background: var(--cream);
    color: var(--ink);
    overflow: hidden;
    touch-action: manipulation;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-family: 'Cormorant Garamond', serif;
}"""

new_body_bg = """html, body {
    width: 100%;
    height: 100%;
    background:
        radial-gradient(ellipse at 15% 10%, rgba(201,168,108,0.07) 0%, transparent 55%),
        radial-gradient(ellipse at 85% 90%, rgba(201,168,108,0.05) 0%, transparent 50%),
        linear-gradient(180deg, var(--marble-snow) 0%, var(--marble-ice) 100%);
    color: var(--ink);
    overflow: hidden;
    touch-action: manipulation;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-family: 'Cormorant Garamond', serif;
}"""

content = content.replace(old_body_bg, new_body_bg)

# ──────────────────────────────────────────────
# 3. BODY OVERLAYS (paper grain -> marble grain)
# ──────────────────────────────────────────────
old_before = """body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(201, 168, 108, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 80% 80%, rgba(201, 138, 138, 0.04) 0%, transparent 40%),
        url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.05'/%3E%3C/svg%3E");
    background-size: cover, cover, 200px 200px;
    pointer-events: none;
    z-index: 9500;
    mix-blend-mode: multiply;
}"""

new_before = """body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.78  0 0 0 0 0.71  0 0 0 0 0.58  0 0 0 0.18 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"),
        url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    background-size: 600px 600px, 200px 200px;
    pointer-events: none;
    z-index: 9500;
    mix-blend-mode: multiply;
}"""

content = content.replace(old_before, new_before)

old_after = """body::after {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at center, transparent 55%, rgba(62, 45, 40, 0.10) 100%),
        radial-gradient(ellipse at top, rgba(201, 168, 108, 0.05), transparent 60%);
    pointer-events: none;
    z-index: 9600;
}"""

new_after = """body::after {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at center, transparent 55%, rgba(50, 45, 35, 0.08) 100%),
        radial-gradient(ellipse at top, rgba(201, 168, 108, 0.08), transparent 60%);
    pointer-events: none;
    z-index: 9600;
}"""

content = content.replace(old_after, new_after)

# ──────────────────────────────────────────────
# 4. PAGE BACKGROUND: cream -> marble white
# ──────────────────────────────────────────────
old_page = r""".page {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 80px 26px 110px;
    overflow-y: auto;
    overflow-x: hidden;
    background:
        linear-gradient(180deg, #fffdf9 0%, var(--cream) 50%, var(--paper) 100%);
    opacity: 0;
    pointer-events: none;
    backface-visibility: hidden;
    transform-origin: left center;
    transform: translateZ(0);
    will-change: transform, opacity;
    scrollbar-width: none;
    -ms-overflow-style: none;
}"""

new_page = r""".page {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 80px 26px 110px;
    overflow-y: auto;
    overflow-x: hidden;
    background:
        linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 40%, var(--marble-cloud) 100%);
    opacity: 0;
    pointer-events: none;
    backface-visibility: hidden;
    transform-origin: left center;
    transform: translateZ(0);
    will-change: transform, opacity;
    scrollbar-width: none;
    -ms-overflow-style: none;
}"""

content = content.replace(old_page, new_page)

# Add marble vein inner shine to .page
page_inner_add = r"""
.page::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 800 800' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='v'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.008' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.80  0 0 0 0 0.73  0 0 0 0 0.60  0 0 0 0.10 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23v)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.8;
    pointer-events: none;
    z-index: 1;
}
.page > * { position: relative; z-index: 2; }
"""
content = content.replace(new_page, new_page + page_inner_add)

# ──────────────────────────────────────────────
# 5. PROGRESS DOTS: pink -> gold
# ──────────────────────────────────────────────
old_pdot = """.pdot.active {
    background: var(--dusty-pink-deep);
    border-color: var(--dusty-pink-deep);
    transform: scale(1.4);
}"""

new_pdot = """.pdot.active {
    background: linear-gradient(145deg, var(--gold), var(--gold-deep));
    border-color: var(--gold-deep);
    transform: scale(1.4);
    box-shadow: 0 0 8px var(--shadow-gold);
}"""

content = content.replace(old_pdot, new_pdot)

# ──────────────────────────────────────────────
# 6. POLAROID -> MARBLE FRAME
# ──────────────────────────────────────────────
old_polaroid_block = r"""/* ─── POLAROIDS ─── */
.polaroid {
    background: linear-gradient(145deg, #ffffff 0%, #fdfbf7 40%, #f9f4ea 100%);
    border: 1px solid rgba(62, 45, 40, 0.06);
    padding: 10px 10px 46px;
    position: relative;
    display: inline-block;
    box-shadow:
        0 2px 4px var(--shadow-soft),
        0 10px 24px var(--shadow-medium);
    max-width: 100%;
    z-index: 100;
}

.polaroid img {
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid rgba(62, 45, 40, 0.08);
    object-fit: cover;
}

.polaroid .cap {
    position: absolute;
    bottom: 10px;
    left: 8px;
    right: 8px;
    text-align: center;
    font-family: 'Caveat', cursive;
    font-size: 16px;
    font-weight: 500;
    color: var(--ink-soft);
    letter-spacing: 0.01em;
    padding-top: 4px;
    border-top: 1px dashed var(--gold-soft);
    margin-top: 4px;
}"""

new_marble_block = r"""/* ─── MARBLE PHOTO FRAMES ─── */
.polaroid {
    background:
        linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 40%, var(--marble-cloud) 100%);
    padding: 18px;
    position: relative;
    display: inline-block;
    box-shadow:
        inset 0 0 0 1px var(--gold-light),
        0 2px 6px var(--shadow-soft),
        0 14px 36px var(--shadow-medium),
        0 2px 14px var(--shadow-gold);
    max-width: 100%;
    z-index: 100;
    border-radius: 2px;
}
.polaroid::before {
    content: '';
    position: absolute;
    inset: 8px;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='mv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.22 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23mv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.85;
    pointer-events: none;
    z-index: 1;
    border-radius: 1px;
}
.polaroid::after {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold-champagne);
    opacity: 0.9;
    pointer-events: none;
    z-index: 3;
    border-radius: 1px;
}
.polaroid img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
    position: relative;
    z-index: 2;
    border: 1px solid rgba(201,168,108,0.25);
    box-shadow: inset 0 0 0 3px #ffffff;
}
.polaroid .cap {
    position: relative;
    bottom: auto;
    left: auto;
    right: auto;
    margin-top: 14px;
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    font-weight: 600;
    font-style: italic;
    color: var(--gold-deep);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 10px 6px 2px;
    border-top: 1px solid var(--gold-champagne);
    position: relative;
    z-index: 4;
}
.polaroid .cap::before,
.polaroid .cap::after {
    content: '❦';
    position: absolute;
    top: -8px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--marble-ice);
    color: var(--gold);
    font-size: 12px;
    padding: 0 10px;
    line-height: 1;
}"""

content = content.replace(old_polaroid_block, new_marble_block)

# ──────────────────────────────────────────────
# 7. REMOVE TAPE (hide it elegantly — marble doesn't need tape)
# ──────────────────────────────────────────────
# Find tape block & replace with invisible render
old_tape_block = r""".tape {
    display: block;
    background: var(--tape);
    height: 22px;
    width: 68px;
    position: absolute;
    top: -11px;
    left: 50%;
    transform: translateX(-50%) rotate(-3deg);
    z-index: 105;
    box-shadow:
        inset 0 1px 2px rgba(255,255,255,0.5),
        0 1px 2px var(--shadow-soft);
    backdrop-filter: blur(2px);
    -webkit-backdrop-filter: blur(2px);
}

.tape.left {
    left: 18px;
    transform: rotate(-10deg);
    width: 52px;
    height: 18px;
}

.tape.right {
    left: auto;
    right: 18px;
    transform: rotate(8deg);
    width: 52px;
    height: 18px;
    background: var(--tape-pink);
}

.tape.corner-tl {
    left: 12px;
    top: -8px;
    transform: rotate(-22deg);
    width: 42px;
    height: 16px;
}

.tape.corner-tr {
    left: auto;
    right: 12px;
    top: -8px;
    transform: rotate(20deg);
    width: 42px;
    height: 16px;
    background: var(--tape-pink);
}"""

new_tape_block = r""".tape {
    display: block;
    height: 22px;
    width: 68px;
    position: absolute;
    top: -11px;
    left: 50%;
    transform: translateX(-50%) rotate(-3deg);
    z-index: 105;
    background: linear-gradient(180deg, var(--gold-light) 0%, var(--gold-champagne) 100%);
    border: 1px solid var(--gold);
    opacity: 0.0;
    pointer-events: none;
}
.tape.left, .tape.right, .tape.corner-tl, .tape.corner-tr { opacity: 0; pointer-events: none; display: none; }
"""

content = content.replace(old_tape_block, new_tape_block)

# Also, remove any <span class="tape">...</span> DOM elements that render.
# Hide them via display:none for marble aesthetic:
content = content.replace('class="tape left"', 'class="tape left" style="display:none"')
content = content.replace('class="tape right"', 'class="tape right" style="display:none"')
content = content.replace('class="tape corner-tl"', 'class="tape corner-tl" style="display:none"')
content = content.replace('class="tape corner-tr"', 'class="tape corner-tr" style="display:none"')
# Also the centered tape (usually no class modifier):
# Keep a regex for <span class="tape"> with no extra class
content = re.sub(r'<span class="tape">', r'<span class="tape" style="display:none">', content)

# ──────────────────────────────────────────────
# 8. TYPOGRAPHY: pink titles -> gold titles
# ──────────────────────────────────────────────
old_bigtitle = r""".big-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(48px, 14vw, 88px);
    color: var(--dusty-pink-deep);
    font-weight: 700;
    line-height: 1;
    margin-bottom: 10px;
    z-index: 100;
    position: relative;
    text-shadow: 0 2px 8px rgba(201, 138, 138, 0.12);"""

new_bigtitle = r""".big-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(48px, 14vw, 88px);
    background: linear-gradient(145deg, var(--gold-deep) 0%, var(--gold) 45%, var(--gold-bright) 70%, var(--gold-soft) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 10px;
    z-index: 100;
    position: relative;
    text-shadow: 0 2px 12px rgba(201, 168, 108, 0.18);"""

content = content.replace(old_bigtitle, new_bigtitle)

# Also handle all inline dusty-pink-deep refs in headings
# We'll use CSS color variable swap via replace-all
content = content.replace('color: var(--dusty-pink-deep)', 'color: var(--gold-deep)')
content = content.replace('color: var(--dusty-pink-soft)', 'color: var(--gold-soft)')
content = content.replace('background: var(--dusty-pink-deep)', 'background: var(--gold-deep)')
content = content.replace('border: 2px solid var(--dusty-pink-deep)', 'border: 2px solid var(--gold-deep)')
content = content.replace('border: 1px solid var(--dusty-pink-deep)', 'border: 1px solid var(--gold-deep)')
content = content.replace('background: linear-gradient(135deg, var(--dusty-pink-soft)', 'background: linear-gradient(135deg, var(--marble-cloud)')
content = content.replace('background: var(--dusty-pink-soft)', 'background: var(--gold-light)')
content = content.replace('var(--dusty-pink-deep)', 'var(--gold-deep)')
content = content.replace('var(--dusty-pink-soft)', 'var(--gold-soft)')
content = content.replace('var(--dusty-pink)', 'var(--gold)')
content = content.replace('var(--blush)', 'var(--marble-cloud)')

# Shadow references that mention rgb(201, 138, 138)
content = content.replace('rgba(201, 138, 138, 0.12)', 'rgba(201, 168, 108, 0.20)')
content = content.replace('rgba(201, 138, 138, 0.04)', 'rgba(201, 168, 108, 0.05)')
content = content.replace('rgba(201, 138, 138, 0.10)', 'rgba(201, 168, 108, 0.14)')

# Old cream references - swap base colours out for marble
content = content.replace('var(--cream-dark)', 'var(--marble-cloud)')
content = content.replace('var(--paper-dark)', 'var(--marble-vein)')
content = content.replace('var(--paper)', 'var(--marble-snow)')
content = content.replace('var(--beige)', 'var(--marble-snow)')
content = content.replace('var(--champagne)', 'var(--gold-champagne)')
content = content.replace('background: var(--cream);', 'background: var(--marble-ice);')
content = content.replace("background: var(--cream)\n", "background: var(--marble-ice)\n")
# Safe var(--cream) swap for the remaining references
content = content.replace('var(--cream)', 'var(--marble-white)')

# ──────────────────────────────────────────────
# 9. STATIONERY (letter) restyle to marble & gold
# ──────────────────────────────────────────────
old_stationery = r""".stationery {
    background: linear-gradient(180deg, #fffdf9 0%, var(--cream) 100%);
    border: 1px solid var(--champagne);
    padding: 34px 26px 30px;
    max-width: 100%;
    width: 100%;
    position: relative;
    text-align: left;
    box-shadow:
        0 2px 6px var(--shadow-soft),
        0 18px 44px var(--shadow-medium);
    margin-top: 12px;
    z-index: 100;
    border-radius: 1px;
}

.stationery::before {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold-soft);
    opacity: 0.4;
    pointer-events: none;
}

.stationery::after {
    content: '';
    position: absolute;
    left: 44px;
    top: 24px;
    bottom: 24px;
    width: 1px;
    background: var(--dusty-pink-soft);
    opacity: 0.4;
    pointer-events: none;
}"""

new_stationery = r""".stationery {
    background: linear-gradient(170deg, var(--marble-white) 0%, var(--marble-ice) 55%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 34px 26px 30px;
    max-width: 100%;
    width: 100%;
    position: relative;
    text-align: left;
    box-shadow:
        inset 0 0 0 6px var(--marble-ice),
        inset 0 0 0 7px var(--gold-champagne),
        0 2px 6px var(--shadow-soft),
        0 18px 44px var(--shadow-medium);
    margin-top: 12px;
    z-index: 100;
    border-radius: 2px;
}
.stationery::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='sv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.08 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23sv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
    z-index: 1;
    border-radius: 1px;
}
.stationery::after {
    content: '';
    position: absolute;
    left: 54px;
    top: 30px;
    bottom: 30px;
    width: 1px;
    background: linear-gradient(180deg, transparent, var(--gold) 10%, var(--gold) 90%, transparent);
    opacity: 0.55;
    pointer-events: none;
    z-index: 2;
}
.stationery .letter-text, .stationery .letter-sig, .stationery > * { position: relative; z-index: 3; }"""

content = content.replace(old_stationery, new_stationery)

# ──────────────────────────────────────────────
# 10. TIMELINE restyle to gold & marble
# ──────────────────────────────────────────────
old_timeline = r""".timeline::before {
    content: '';
    position: absolute;
    left: 24px;
    top: 20px;
    bottom: 20px;
    width: 2px;
    background:
        linear-gradient(180deg,
            transparent 0%,
            var(--gold-soft) 8%,
            var(--dusty-pink-soft) 50%,
            var(--gold-soft) 92%,
            transparent 100%);
    opacity: 0.7;
}"""

new_timeline = r""".timeline::before {
    content: '';
    position: absolute;
    left: 24px;
    top: 20px;
    bottom: 20px;
    width: 2px;
    background:
        linear-gradient(180deg,
            transparent 0%,
            var(--gold-champagne) 8%,
            var(--gold) 50%,
            var(--gold-champagne) 92%,
            transparent 100%);
    opacity: 0.85;
    box-shadow: 0 0 4px var(--shadow-gold);
}"""

content = content.replace(old_timeline, new_timeline)

# tl-dot restyle
old_tldot = r""".tl-dot {
    position: absolute;
    left: 14px;
    top: 4px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--cream);
    border: 2px solid var(--gold-deep);
    box-shadow:
        0 0 0 4px var(--cream),
        0 2px 6px var(--shadow-soft);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    z-index: 2;
}"""

new_tldot = r""".tl-dot {
    position: absolute;
    left: 14px;
    top: 4px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, var(--gold-light) 0%, var(--gold) 70%, var(--gold-deep) 100%);
    border: 2px solid var(--marble-white);
    box-shadow:
        0 0 0 3px var(--gold-champagne),
        0 0 10px var(--shadow-gold),
        0 2px 6px var(--shadow-soft);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    color: var(--marble-white);
    z-index: 2;
}"""

content = content.replace(old_tldot, new_tldot)

# ──────────────────────────────────────────────
# 11. STAT CARDS: marble & gold
# ──────────────────────────────────────────────
old_stat = r""".stat-card {
    background: linear-gradient(145deg, #fffdf9 0%, var(--cream-dark) 100%);
    border: 1px solid var(--champagne);
    padding: 18px 10px 16px;
    text-align: center;
    position: relative;
    box-shadow:
        0 2px 5px var(--shadow-soft),
        0 8px 20px var(--shadow-soft);
    border-radius: 2px;
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 8px;
    left: 8px;
    right: 8px;
    bottom: 8px;
    border: 1px dashed var(--gold-soft);
    opacity: 0.5;
    pointer-events: none;
}

.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: clamp(26px, 8vw, 34px);
    font-weight: 700;
    color: var(--gold-deep);
    line-height: 1.1;
    margin-bottom: 4px;
    position: relative;
    z-index: 2;
}"""

new_stat = r""".stat-card {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 50%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 20px 10px 18px;
    text-align: center;
    position: relative;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 8px 22px var(--shadow-medium),
        0 0 16px var(--shadow-gold);
    border-radius: 2px;
}
.stat-card::before {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold-champagne);
    opacity: 0.85;
    pointer-events: none;
    z-index: 1;
}
.stat-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='st'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.83  0 0 0 0 0.77  0 0 0 0 0.65  0 0 0 0.10 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23st)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
    z-index: 0;
    border-radius: 1px;
}
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: clamp(26px, 8vw, 34px);
    font-weight: 700;
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
    margin-bottom: 4px;
    position: relative;
    z-index: 2;
    letter-spacing: 0.01em;
}"""

content = content.replace(old_stat, new_stat)

# ──────────────────────────────────────────────
# 12. DIARY / NOTEBOOK pages restyle
# ──────────────────────────────────────────────
old_nb = r""".notebook-page {
    width: 100%;
    max-width: 100%;
    padding: 26px 24px 26px 44px;
    margin-top: 12px;
    background:
        linear-gradient(180deg, #fffdf9 0%, var(--cream) 100%);
    position: relative;
    border: 1px solid var(--champagne);
    box-shadow:
        0 2px 6px var(--shadow-soft),
        0 14px 34px var(--shadow-medium);
    z-index: 100;
    border-radius: 1px;
}

.notebook-page::before {
    content: '';
    position: absolute;
    left: 34px;
    top: 0;
    bottom: 0;
    width: 1px;
    background: var(--dusty-pink-soft);
    opacity: 0.5;
}

.notebook-page::after {
    content: '';
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    width: 30px;
    background: linear-gradient(90deg, transparent 0%, var(--paper-dark) 100%);
    opacity: 0.15;
}"""

new_nb = r""".notebook-page {
    width: 100%;
    max-width: 100%;
    padding: 28px 24px 28px 48px;
    margin-top: 12px;
    background: linear-gradient(170deg, var(--marble-white) 0%, var(--marble-ice) 55%, var(--marble-cloud) 100%);
    position: relative;
    border: 1px solid var(--gold-champagne);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 14px 34px var(--shadow-medium),
        0 0 18px var(--shadow-gold);
    z-index: 100;
    border-radius: 2px;
}
.notebook-page::before {
    content: '';
    position: absolute;
    left: 38px;
    top: 0;
    bottom: 0;
    width: 1px;
    background: linear-gradient(180deg, transparent, var(--gold) 8%, var(--gold) 92%, transparent);
    opacity: 0.6;
}
.notebook-page::after {
    content: '';
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    width: 30px;
    background:
        linear-gradient(90deg, transparent 0%, var(--marble-vein) 100%);
    opacity: 0.2;
}
.notebook-page > * { position: relative; z-index: 2; }"""

content = content.replace(old_nb, new_nb)

# notebook holes -> gold rings
old_holes = r""".notebook-holes {
    position: absolute;
    left: 8px;
    top: 40px;
    bottom: 40px;
    width: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    z-index: 2;
    pointer-events: none;
}

.notebook-holes span {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: var(--cream);
    border: 1px solid var(--gold-soft);
    box-shadow:
        inset 0 2px 3px var(--shadow-soft),
        0 1px 1px rgba(255,255,255,0.6);
}"""

new_holes = r""".notebook-holes {
    position: absolute;
    left: 10px;
    top: 40px;
    bottom: 40px;
    width: 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    z-index: 2;
    pointer-events: none;
}
.notebook-holes span {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background:
        radial-gradient(circle at 35% 35%, var(--gold-light) 0%, var(--gold) 50%, var(--gold-deep) 100%);
    box-shadow:
        inset 0 1px 2px rgba(255,255,255,0.5),
        0 0 0 3px var(--marble-ice),
        0 0 8px var(--shadow-gold),
        0 2px 4px var(--shadow-soft);
    position: relative;
}
.notebook-holes span::after {
    content: '';
    position: absolute;
    inset: 4px;
    border-radius: 50%;
    background: var(--marble-white);
    box-shadow: inset 0 1px 2px var(--shadow-soft);
}"""

content = content.replace(old_holes, new_holes)

# notebook heading (handwritten) -> gold
# Also change .nb-title (if we find it) color - let's search first later.
# For things-list numbers: was dusty-pink-deep, already handled by find/replace above.

# ──────────────────────────────────────────────
# 13. MEMORY PAGES diary section
# ──────────────────────────────────────────────
old_mem = r""".diary {
    margin-top: 18px;
    width: 100%;
    padding: 26px 22px 24px 40px;
    position: relative;
    background:
        linear-gradient(180deg, #fffdfa 0%, var(--cream) 100%);
    border: 1px solid var(--champagne);
    box-shadow:
        0 2px 5px var(--shadow-soft),
        0 12px 32px var(--shadow-medium);
    z-index: 100;
}"""

new_mem = r""".diary {
    margin-top: 18px;
    width: 100%;
    padding: 28px 22px 26px 46px;
    position: relative;
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 55%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 5px var(--shadow-soft),
        0 12px 32px var(--shadow-medium),
        0 0 14px var(--shadow-gold);
    z-index: 100;
}
.diary::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='dv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.09 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23dv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
    z-index: 1;
}
.diary > * { position: relative; z-index: 2; }"""

content = content.replace(old_mem, new_mem)

# ──────────────────────────────────────────────
# 14. NAV BUTTONS -> marble & gold
# ──────────────────────────────────────────────
old_navbtn = r""".nav-btn {
    background: var(--cream);
    border: 1px solid var(--gold);
    color: var(--ink-soft);
    padding: 10px 18px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    cursor: pointer;
    box-shadow: 0 2px 6px var(--shadow-soft);
    transition: all 0.3s ease;
    border-radius: 1px;
}

.nav-btn:hover, .nav-btn:active {
    background: var(--beige);
    color: var(--ink);
    transform: translateY(-1px);
    box-shadow: 0 6px 16px var(--shadow-medium);
}"""

new_navbtn = r""".nav-btn {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold);
    color: var(--gold-deep);
    padding: 10px 18px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    cursor: pointer;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 0 10px var(--shadow-gold);
    transition: all 0.3s ease;
    border-radius: 2px;
}
.nav-btn:hover, .nav-btn:active {
    background: linear-gradient(160deg, var(--marble-cloud) 0%, var(--marble-ice) 100%);
    color: var(--ink);
    transform: translateY(-2px);
    box-shadow:
        inset 0 0 0 1px var(--gold-light),
        0 8px 20px var(--shadow-medium),
        0 0 18px var(--shadow-gold);
}"""

content = content.replace(old_navbtn, new_navbtn)

# ──────────────────────────────────────────────
# 15. MUSIC CONTROLS -> marble & gold
# ──────────────────────────────────────────────
old_music = r""".music-wrap {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 9800;
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--cream);
    border: 1px solid var(--gold-soft);
    padding: 8px 12px;
    border-radius: 28px;
    box-shadow: 0 2px 12px var(--shadow-soft);
}"""

new_music = r""".music-wrap {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 9800;
    display: flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 8px 12px;
    border-radius: 28px;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 10px var(--shadow-soft),
        0 0 14px var(--shadow-gold);
}"""

content = content.replace(old_music, new_music)

old_musbtn = r""".mus-btn {
    background: var(--beige);
    border: 1px solid var(--gold-soft);
    color: var(--gold-deep);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    box-shadow: 0 2px 6px var(--shadow-soft);
    transition: all 0.25s ease;
    padding: 0;
    flex-shrink: 0;
}"""

new_musbtn = r""".mus-btn {
    background: linear-gradient(145deg, var(--marble-ice), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    color: var(--gold-deep);
    width: 30px;
    height: 30px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 0 8px var(--shadow-gold);
    transition: all 0.25s ease;
    padding: 0;
    flex-shrink: 0;
}"""

content = content.replace(old_musbtn, new_musbtn)

# Volume bar -> gold
old_vol = r""".vol {
    -webkit-appearance: none;
    appearance: none;
    width: 90px;
    height: 4px;
    background: var(--champagne);
    border-radius: 2px;
    outline: none;
}"""

new_vol = r""".vol {
    -webkit-appearance: none;
    appearance: none;
    width: 90px;
    height: 4px;
    background: linear-gradient(90deg, var(--gold-light), var(--gold-champagne));
    border-radius: 2px;
    outline: none;
}"""

content = content.replace(old_vol, new_vol)

# Vol thumb
old_thumb = r"""input[type="range"].vol::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--gold-deep);
    border: 2px solid var(--cream);
    cursor: pointer;
    box-shadow: 0 2px 4px var(--shadow-soft);
}"""

new_thumb = r"""input[type="range"].vol::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, var(--gold-light), var(--gold) 60%, var(--gold-deep));
    border: 2px solid var(--marble-white);
    cursor: pointer;
    box-shadow:
        0 0 0 1px var(--gold-champagne),
        0 0 6px var(--shadow-gold),
        0 2px 4px var(--shadow-soft);
}"""

content = content.replace(old_thumb, new_thumb)

# Home button
old_home = r""".home-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 9799;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: var(--cream);
    border: 1px solid var(--gold-soft);
    color: var(--gold-deep);
    font-size: 16px;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px var(--shadow-soft);
    transition: all 0.25s ease;
    padding: 0;
}"""

new_home = r""".home-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 9799;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: linear-gradient(145deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    color: var(--gold-deep);
    font-size: 16px;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 8px var(--shadow-soft),
        0 0 10px var(--shadow-gold);
    transition: all 0.25s ease;
    padding: 0;
}"""

content = content.replace(old_home, new_home)

# ──────────────────────────────────────────────
# 16. LOADING SCREEN book: marble + gold
# ──────────────────────────────────────────────
old_load = r""".load-book .book-cover,
.load-book .book-page {
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, var(--marble-cloud) 0%, var(--marble-white) 50%, var(--marble-vein) 100%);
    border: 1px solid var(--champagne);
    box-shadow:
        inset 0 0 0 3px var(--marble-white),
        0 10px 30px var(--shadow-medium);
    border-radius: 2px 6px 6px 2px;
    transform-origin: left center;
}

.load-book .book-cover {
    background: linear-gradient(135deg, var(--marble-cloud) 0%, var(--marble-cloud) 50%, var(--marble-white) 100%);
    animation: book-open 2.4s cubic-bezier(0.65, 0.05, 0.36, 1) infinite;
}

.load-book .book-spine {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 8px;
    background: linear-gradient(90deg, var(--gold-deep), var(--gold));
    border-radius: 2px 0 0 2px;
}"""

# Note: above pattern won't match because we already substituted var(--cream) → var(--marble-white) and var(--champagne) etc.
# Let's use a fresh pattern. Actually the original was dusty-pink; after find/replace earlier it says var(--marble-cloud) which we did above.
# So let's write an improved version and find the actual current string:

# We already have variables replaced, so let's just search for "book-cover" block and update it via regex:
content = re.sub(
    r"""\.load-book \.book-cover,
\.load-book \.book-page \{
    position: absolute;
    inset: 0;
    background: linear-gradient\(135deg, var\(--marble-cloud\) 0%, var\(--marble-white\) 50%, var\(--marble-vein\) 100%\);
    border: 1px solid var\(--gold-champagne\);
    box-shadow:
        inset 0 0 0 3px var\(--marble-white\),
        0 10px 30px var\(--shadow-medium\);
    border-radius: 2px 6px 6px 2px;
    transform-origin: left center;
\}

\.load-book \.book-cover \{
    background: linear-gradient\(135deg, var\(--marble-cloud\) 0%, var\(--marble-cloud\) 50%, var\(--marble-white\) 100%\);
    animation: book-open 2\.4s cubic-bezier\(0\.65, 0\.05, 0\.36, 1\) infinite;
\}

\.load-book \.book-spine \{
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 8px;
    background: linear-gradient\(90deg, var\(--gold-deep\), var\(--gold\)\);
    border-radius: 2px 0 0 2px;
\}""",
    r""".load-book .book-cover,
.load-book .book-page {
    position: absolute;
    inset: 0;
    background:
        linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 50%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    box-shadow:
        inset 0 0 0 3px var(--marble-white),
        inset 0 0 0 4px var(--gold-champagne),
        0 10px 30px var(--shadow-medium),
        0 0 20px var(--shadow-gold);
    border-radius: 2px 6px 6px 2px;
    transform-origin: left center;
}
.load-book .book-cover::before,
.load-book .book-page::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='bv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.22 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23bv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    border-radius: 2px 6px 6px 2px;
}
.load-book .book-cover {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-cloud) 50%, var(--marble-vein) 100%);
    animation: book-open 2.4s cubic-bezier(0.65, 0.05, 0.36, 1) infinite;
}
.load-book .book-cover::after {
    content: '';
    position: absolute;
    inset: 12px;
    border: 1px solid var(--gold);
    z-index: 2;
    opacity: 0.85;
    border-radius: 1px 4px 4px 1px;
}
.load-book .book-spine {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 10px;
    background: linear-gradient(90deg, var(--gold-deep) 0%, var(--gold) 50%, var(--gold-bright) 100%);
    border-radius: 2px 0 0 2px;
    z-index: 2;
    box-shadow: 1px 0 0 var(--gold-champagne);
}""",
    content
)

# ──────────────────────────────────────────────
# 17. FUTURE cards (p15) restyle
# ──────────────────────────────────────────────
old_future = r""".future-item {
    background: linear-gradient(145deg, #fffdf9 0%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 20px 18px 18px;
    position: relative;
    box-shadow:
        0 2px 5px var(--shadow-soft),
        0 8px 18px var(--shadow-soft);
    border-radius: 2px;
    margin-bottom: 16px;
}"""

new_future = r""".future-item {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 55%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 22px 18px 20px;
    position: relative;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 5px var(--shadow-soft),
        0 8px 20px var(--shadow-medium),
        0 0 16px var(--shadow-gold);
    border-radius: 2px;
    margin-bottom: 16px;
}
.future-item::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='fv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.10 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23fv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
    z-index: 1;
}
.future-item::after {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold-champagne);
    opacity: 0.85;
    pointer-events: none;
    z-index: 2;
}
.future-item > * { position: relative; z-index: 3; }"""

content = content.replace(old_future, new_future)

# ──────────────────────────────────────────────
# 18. FLOWER NOTE modal: marble & gold
# ──────────────────────────────────────────────
old_fn = r""".flower-note {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.9);
    background: var(--marble-white);
    border: 1px solid var(--gold);
    padding: 22px 24px;
    font-family: 'Caveat', cursive;
    font-size: 18px;
    color: var(--ink);
    box-shadow: 0 20px 60px var(--shadow-deep);
    z-index: 9990;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease, transform 0.3s ease;
    max-width: 84%;
    text-align: center;
    line-height: 1.5;
    border-radius: 2px;
}"""

new_fn = r""".flower-note {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.9);
    background: linear-gradient(160deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold);
    padding: 22px 24px;
    font-family: 'Caveat', cursive;
    font-size: 18px;
    color: var(--ink);
    box-shadow:
        inset 0 0 0 6px var(--marble-ice),
        inset 0 0 0 7px var(--gold-champagne),
        0 20px 60px var(--shadow-deep),
        0 0 30px var(--shadow-gold);
    z-index: 9990;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease, transform 0.3s ease;
    max-width: 84%;
    text-align: center;
    line-height: 1.5;
    border-radius: 2px;
}"""

content = content.replace(old_fn, new_fn)

# flower-note close button
old_fnc = r"""    border: 1px solid var(--gold-soft);"""
new_fnc = r"""    border: 1px solid var(--gold);
    background: linear-gradient(145deg, var(--marble-white), var(--marble-cloud));
    color: var(--gold-deep);"""
content = content.replace('.fn-close {\n    margin-top: 14px;\n    font-family: \'Cormorant Garamond\', serif;\n    font-size: 11px;\n    letter-spacing: 0.2em;\n    text-transform: uppercase;\n    color: var(--ink-faint);\n    cursor: pointer;\n    display: inline-block;\n    padding: 4px 12px;\n    border: 1px solid var(--gold-soft);\n}',
    '.fn-close {\n    margin-top: 14px;\n    font-family: \'Cormorant Garamond\', serif;\n    font-size: 11px;\n    letter-spacing: 0.2em;\n    text-transform: uppercase;\n    color: var(--gold-deep);\n    cursor: pointer;\n    display: inline-block;\n    padding: 4px 14px;\n    background: linear-gradient(145deg, var(--marble-white), var(--marble-cloud));\n    border: 1px solid var(--gold-champagne);\n    border-radius: 1px;\n    box-shadow: 0 2px 6px var(--shadow-soft);\n}'
)

# flower-note ♡ -> ❦ (golden fleuron)
content = content.replace("content: '♡';\n    display: block;\n    font-size: 14px;\n    color: var(--gold-deep);",
    "content: '❦';\n    display: block;\n    font-size: 16px;\n    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));\n    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;")

# ──────────────────────────────────────────────
# 19. THANKS + ENDING pages style
# ──────────────────────────────────────────────
old_thanks = r""".thanks-wrap {
    background: linear-gradient(145deg, #fffdf9 0%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold);
    padding: 40px 28px;
    max-width: 100%;
    text-align: center;
    box-shadow: 0 20px 60px var(--shadow-deep);
    border-radius: 2px;
    z-index: 100;
}"""

new_thanks = r""".thanks-wrap {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 55%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 40px 28px;
    max-width: 100%;
    text-align: center;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 20px 60px var(--shadow-deep),
        0 0 26px var(--shadow-gold);
    border-radius: 2px;
    z-index: 100;
    position: relative;
}
.thanks-wrap::before {
    content: '';
    position: absolute;
    inset: 8px;
    border: 1px solid var(--gold-champagne);
    opacity: 0.85;
    pointer-events: none;
}
.thanks-wrap::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='tv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.11 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23tv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
}
.thanks-wrap > * { position: relative; z-index: 2; }"""

content = content.replace(old_thanks, new_thanks)

# same for ending-wrap
old_ending = r""".ending-wrap {
    background: linear-gradient(145deg, #fffdf9 0%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-soft);
    padding: 30px 22px;
    max-width: 100%;
    width: 100%;
    text-align: center;
    box-shadow: 0 4px 12px var(--shadow-medium);
    z-index: 100;
}"""

new_ending = r""".ending-wrap {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 55%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 30px 22px;
    max-width: 100%;
    width: 100%;
    text-align: center;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 4px 12px var(--shadow-medium),
        0 0 18px var(--shadow-gold);
    z-index: 100;
    position: relative;
}
.ending-wrap::before {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold-champagne);
    opacity: 0.85;
    pointer-events: none;
}
.ending-wrap::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='ev'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.10 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23ev)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
}
.ending-wrap > * { position: relative; z-index: 2; }"""

content = content.replace(old_ending, new_ending)

# ──────────────────────────────────────────────
# 20. SCATTERED POLAROIDS (side minis): marble too
# ──────────────────────────────────────────────
# Find the JS scatter function, change the innerHTML to marble-style
old_scatter_inner = r"""            div.innerHTML = `<img src="${pic}" style="padding:4px 4px 14px; background:#fff; border:1px solid rgba(62,45,40,0.05); box-shadow:0 2px 6px var(--shadow-soft);">`;"""

new_scatter_inner = r"""            div.innerHTML = `<img src="${pic}" style="padding:5px; background:linear-gradient(160deg,#ffffff,#f5f7fa,#eef1f6); border:1px solid var(--gold-champagne); box-shadow:inset 0 0 0 1px #ffffff, 0 2px 6px var(--shadow-soft), 0 0 8px var(--shadow-gold);">`;"""
content = content.replace(old_scatter_inner, new_scatter_inner)

# ──────────────────────────────────────────────
# 21. PAGE-TURN shadows: update to marble
# ──────────────────────────────────────────────
content = content.replace(
    'box-shadow: 20px 0 40px var(--shadow-deep);',
    'box-shadow: 20px 0 40px var(--shadow-deep), 0 0 30px var(--shadow-gold);'
)
content = content.replace(
    'box-shadow: 50px 0 80px var(--shadow-deep);',
    'box-shadow: 50px 0 80px var(--shadow-deep), 0 0 50px var(--shadow-gold);'
)

# ──────────────────────────────────────────────
# 22. Pressed Flower colours: make them gold
# (Emojis stay, but adjust opacity/rotation)
# ──────────────────────────────────────────────
# Already handled implicitly via opacity + tint. Keep as-is.

# ──────────────────────────────────────────────
# 23. Open Album button styling
# ──────────────────────────────────────────────
content = content.replace(
    """background: var(--marble-white);
    border: 1px solid var(--gold);
    padding: 14px 32px;
    font-size: 16px;
    letter-spacing: 0.24em;
    box-shadow: 0 6px 20px var(--shadow-medium);
    cursor: pointer;
    border-radius: 1px;
    transition: all 0.35s ease;
    z-index: 100;
}
#open-album:hover, #open-album:active {
    background: var(--gold-light);
    transform: translateY(-2px);
    box-shadow: 0 12px 30px var(--shadow-deep);
}""",
    """background: linear-gradient(160deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    padding: 14px 32px;
    font-size: 16px;
    letter-spacing: 0.24em;
    color: var(--gold-deep);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold-champagne),
        0 6px 20px var(--shadow-medium),
        0 0 18px var(--shadow-gold);
    cursor: pointer;
    border-radius: 2px;
    transition: all 0.35s ease;
    z-index: 100;
    position: relative;
}
#open-album::after {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold);
    opacity: 0.7;
    pointer-events: none;
    border-radius: 1px;
}
#open-album:hover, #open-album:active {
    background: linear-gradient(160deg, var(--marble-cloud), var(--marble-ice));
    transform: translateY(-2px);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold),
        0 12px 32px var(--shadow-deep),
        0 0 26px var(--shadow-gold);
}"""
)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done - marble & gold aesthetic applied")
