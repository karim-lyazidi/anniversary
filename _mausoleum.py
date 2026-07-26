import json

BG_SITE = "backgroug.jfif"
MOMENTS = ["moment 1.jpg", "moment 2.jpg", "moment 3.jpg", "moment 4.jpg"]
K_BDAY = "14.08.2003.jpg"
A_BDAY = "19.06.2004.jpg"
MEET_NIGHT = "29.07.2025.jpg"
STARS = "stars.png"
MES = [f"me ({i}).jpg" for i in range(1, 11)]
LETTER = "letter.jfif"
GIFTS = ["gifts (1).jpg", "gifts (2).jpg"]
OUR_GIFT = "moment 4.jpg"
BG_DECOS = [
    "bg (1).jfif", "bg (2).jfif", "bg (3).jfif",
    "bg (5).jfif", "bg (6).jfif", "bg (7).jfif", "bg (8).jfif", "bg (9).jfif",
    "bg (10).jfif", "bg (11).jfif", "bg (12).jfif", "bg (13).jfif", "bg (14).jfif",
    "bg (15).jfif", "bg (16).jfif", "bg (17).jfif", "bg (18).jfif", "bg (19).jfif",
    "bg (20).jfif", "bg (21).jfif", "bg (22).jfif", "bg (23).jfif", "bg (24).jfif",
    "bg (25).jfif", "bg (26).jfif", "bg (27).jfif", "bg (28).jfif"
]
MUSIC = "Never Coming Back.mp3"

# --- Build the JS BGS array literal cleanly ---
BGS_LITERAL = json.dumps(BG_DECOS, ensure_ascii=False)  # ["bg (1).jfif", ...]

# --- Asset placeholder substitutions ---
placeholders = {
    "@BG_SITE@": BG_SITE,
    "@M1@": MOMENTS[0], "@M2@": MOMENTS[1], "@M3@": MOMENTS[2], "@M4@": MOMENTS[3],
    "@K_BDAY@": K_BDAY, "@A_BDAY@": A_BDAY, "@MEET@": MEET_NIGHT,
    "@STARS@": STARS,
    "@ME1@": MES[0], "@ME2@": MES[1], "@ME3@": MES[2], "@ME4@": MES[3], "@ME5@": MES[4],
    "@ME6@": MES[5], "@ME7@": MES[6], "@ME8@": MES[7], "@ME9@": MES[8], "@ME10@": MES[9],
    "@LETTER@": LETTER,
    "@G1@": GIFTS[0], "@G2@": GIFTS[1],
    "@OUR_GIFT@": OUR_GIFT,
    "@MUSIC@": MUSIC,
    "@BGS_ARRAY@": BGS_LITERAL
}

# =====================================================
# TEMPLATE (uses {{ for literal braces, @VAR@ for placeholders)
# =====================================================
tpl = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#f9fafb">
<title>Our Mausoleum of Memories ♡ Karim &amp; Aya</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Dancing+Script:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Caveat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
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
    --shadow-deep: rgba(50, 45, 35, 0.22);
    --shadow-gold: rgba(201, 168, 108, 0.20);
    --mausoleum-dark: rgba(20, 18, 14, 0.55);
}

* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

html, body {
    width: 100%;
    height: 100%;
    color: var(--ink);
    overflow: hidden;
    touch-action: manipulation;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-family: 'Cormorant Garamond', serif;
}

body {
    background-color: var(--marble-snow);
    background-image:
        linear-gradient(180deg, rgba(255,255,255,0.88) 0%, rgba(245,247,250,0.92) 55%, rgba(238,241,246,0.96) 100%),
        url("@BG_SITE@");
    background-size: cover, cover;
    background-position: center, center;
    background-attachment: fixed, fixed;
    background-repeat: no-repeat, no-repeat;
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Marble grain overlay (site-wide) */
body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.12 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"),
        url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n2'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n2)' opacity='0.04'/%3E%3C/svg%3E");
    background-size: 600px 600px, 200px 200px;
    pointer-events: none;
    z-index: 9500;
    mix-blend-mode: multiply;
}
body::after {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at center, transparent 45%, rgba(20, 18, 14, 0.14) 100%),
        radial-gradient(ellipse at top, rgba(201, 168, 108, 0.10), transparent 60%);
    pointer-events: none;
    z-index: 9600;
}

.vignette {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9400;
    background:
        radial-gradient(ellipse at 0% 0%, rgba(201,168,108,0.10), transparent 30%),
        radial-gradient(ellipse at 100% 0%, rgba(201,168,108,0.10), transparent 30%),
        radial-gradient(ellipse at 0% 100%, rgba(20,18,14,0.10), transparent 32%),
        radial-gradient(ellipse at 100% 100%, rgba(20,18,14,0.10), transparent 32%);
}

/* MUSIC BAR */
#music-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9800;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.94), rgba(245,247,250,0.92));
    border-bottom: 1px solid var(--gold-champagne);
    padding: 10px 18px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow:
        0 2px 10px var(--shadow-soft),
        0 0 14px var(--shadow-gold);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
}
#music-bar::after {
    content: '';
    position: absolute;
    left: 0; right: 0; bottom: -1px;
    height: 1px;
    background: linear-gradient(90deg, transparent 5%, var(--gold) 50%, transparent 95%);
    opacity: 0.55;
}
.music-track {
    font-family: 'Cormorant Garamond', serif;
    font-size: 13px;
    font-weight: 600;
    color: var(--ink-soft);
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.music-track .note {
    color: var(--gold-deep);
    font-size: 14px;
    animation: note-bounce 2.4s ease-in-out infinite;
}
@keyframes note-bounce {
    0%, 100% { transform: translateY(0) rotate(0); }
    50% { transform: translateY(-2px) rotate(6deg); }
}
.music-controls { margin-left: auto; display: flex; align-items: center; gap: 10px; }
#music-toggle {
    cursor: pointer;
    width: 38px; height: 38px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(145deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    border-radius: 50%;
    font-size: 15px;
    color: var(--gold-deep);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 0 10px var(--shadow-gold);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
#music-toggle:hover { box-shadow: inset 0 0 0 1px var(--gold-light), 0 4px 10px var(--shadow-medium), 0 0 14px var(--shadow-gold); }
#music-toggle:active { transform: scale(0.94); }

#volume-slider {
    width: 68px; height: 3px;
    cursor: pointer;
    background: linear-gradient(90deg, var(--gold-light), var(--gold));
    border-radius: 2px;
    -webkit-appearance: none; appearance: none;
    opacity: 0.95;
    outline: none;
}
#volume-slider::-webkit-slider-thumb {
    -webkit-appearance: none; appearance: none;
    width: 14px; height: 14px; border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, var(--gold-light), var(--gold) 60%, var(--gold-deep));
    border: 2px solid var(--marble-white);
    box-shadow: 0 0 0 1px var(--gold-champagne), 0 0 6px var(--shadow-gold), 0 2px 4px var(--shadow-soft);
    cursor: pointer;
}
#volume-slider::-moz-range-thumb {
    width: 14px; height: 14px; border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, var(--gold-light), var(--gold) 60%, var(--gold-deep));
    border: 2px solid var(--marble-white);
    box-shadow: 0 0 0 1px var(--gold-champagne), 0 0 6px var(--shadow-gold), 0 2px 4px var(--shadow-soft);
    cursor: pointer;
}

/* HOME BUTTON */
#home-btn {
    cursor: pointer;
    width: 38px; height: 38px;
    display: none; align-items: center; justify-content: center;
    background: linear-gradient(145deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    border-radius: 50%;
    font-size: 14px; color: var(--gold-deep);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 0 10px var(--shadow-gold);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    z-index: 9799;
    position: fixed; top: 10px; right: 18px;
}
#home-btn:hover { box-shadow: inset 0 0 0 1px var(--gold-light), 0 4px 10px var(--shadow-medium), 0 0 14px var(--shadow-gold); }
#home-btn.show { display: flex; }
#home-btn:active { transform: scale(0.94); }

/* MAUSOLEUM WALK-THROUGH PAGES CONTAINER */
#pages-wrap {
    position: fixed;
    inset: 0;
    perspective: 1400px;
    perspective-origin: 50% 50%;
    z-index: 1;
}
#pages {
    position: absolute;
    inset: 0;
    transform-style: preserve-3d;
}

.page {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 72px 24px 108px;
    overflow-y: auto;
    overflow-x: hidden;
    opacity: 0;
    pointer-events: none;
    transform: translateZ(-800px) scale(0.96);
    will-change: transform, opacity, filter;
    scrollbar-width: none;
    -ms-overflow-style: none;
}
.page::-webkit-scrollbar { display: none; }
.page > * { position: relative; z-index: 2; }
.page::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        url("data:image/svg+xml,%3Csvg viewBox='0 0 800 800' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='v'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.008' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.09 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23v)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.85;
    pointer-events: none;
    z-index: 1;
}

.page.active {
    opacity: 1;
    pointer-events: all;
    transform: translateZ(0) scale(1);
    filter: blur(0) brightness(1);
    transition:
        transform 1.15s cubic-bezier(0.22, 0.8, 0.30, 1),
        opacity 0.95s cubic-bezier(0.22, 0.8, 0.30, 1),
        filter 1.15s cubic-bezier(0.22, 0.8, 0.30, 1);
}

.page.leaving-back {
    opacity: 0;
    pointer-events: none;
    transform: translateZ(-900px) scale(0.88);
    filter: blur(3px) brightness(0.6);
    transition:
        transform 1.15s cubic-bezier(0.55, 0.06, 0.68, 0.19),
        opacity 0.85s ease-in,
        filter 1.15s ease-in;
}
.page.leaving-fwd {
    opacity: 0;
    pointer-events: none;
    transform: translateZ(600px) scale(1.20);
    filter: blur(2px) brightness(1.25);
    transition:
        transform 1.15s cubic-bezier(0.55, 0.06, 0.68, 0.19),
        opacity 0.85s ease-in,
        filter 1.15s ease-in;
}

.page.entering-back {
    opacity: 0;
    transform: translateZ(600px) scale(1.20);
    filter: blur(2px) brightness(1.25);
}
.page.entering-fwd {
    opacity: 0;
    transform: translateZ(-900px) scale(0.88);
    filter: blur(3px) brightness(0.6);
}

.corridor-fade {
    position: fixed;
    left: 0; right: 0;
    z-index: 9300;
    pointer-events: none;
}
.corridor-fade.top {
    top: 48px;
    height: 40px;
    background: linear-gradient(180deg, rgba(255,255,255,0.65), transparent);
}
.corridor-fade.bottom {
    bottom: 0;
    height: 120px;
    background: linear-gradient(0deg, rgba(20,18,14,0.18), transparent 70%);
}

/* NAV BUTTONS */
.nav-btn {
    position: fixed;
    bottom: 22px;
    background: linear-gradient(160deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    color: var(--gold-deep);
    font-family: 'Cormorant Garamond', serif;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    padding: 12px 22px;
    cursor: pointer;
    z-index: 9700;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold-champagne),
        0 4px 12px var(--shadow-medium),
        0 0 14px var(--shadow-gold);
    transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
    border-radius: 2px;
    min-width: 72px;
    min-height: 44px;
}
.nav-btn:hover {
    background: linear-gradient(160deg, var(--marble-cloud), var(--marble-ice));
    box-shadow:
        inset 0 0 0 1px var(--gold-light),
        inset 0 0 0 2px var(--gold),
        0 6px 16px var(--shadow-medium),
        0 0 18px var(--shadow-gold);
    color: var(--ink);
}
.nav-btn:active { transform: translateY(2px) scale(0.97); }
#btn-prev { left: 16px; }
#btn-next { right: 16px; }
.hidden { opacity: 0; pointer-events: none; transform: scale(0.9); }

/* DOTS (mausoleum chambers) */
#page-dots {
    position: fixed;
    left: 50%;
    bottom: 30px;
    transform: translateX(-50%);
    display: flex;
    gap: 6px;
    align-items: center;
    z-index: 9700;
    padding: 8px 14px;
    background: linear-gradient(145deg, rgba(255,255,255,0.75), rgba(238,241,246,0.75));
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    border: 1px solid var(--gold-champagne);
    border-radius: 999px;
    box-shadow: 0 2px 10px var(--shadow-soft), 0 0 12px var(--shadow-gold);
}
.pdot {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--marble-vein);
    border: 1px solid var(--marble-white);
    cursor: pointer;
    transition: all 0.3s ease;
    flex-shrink: 0;
}
.pdot.active {
    background: linear-gradient(145deg, var(--gold), var(--gold-deep));
    border-color: var(--gold-deep);
    transform: scale(1.5);
    box-shadow: 0 0 8px var(--shadow-gold);
}

/* MARBLE PHOTO FRAME */
.mf {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 40%, var(--marble-cloud) 100%);
    padding: 14px;
    position: relative;
    display: inline-block;
    box-shadow:
        inset 0 0 0 1px var(--gold-light),
        0 2px 6px var(--shadow-soft),
        0 14px 36px var(--shadow-medium),
        0 2px 14px var(--shadow-gold);
    max-width: 100%;
    border-radius: 2px;
}
.mf::before {
    content: '';
    position: absolute;
    inset: 7px;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='mv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.20 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23mv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.85;
    pointer-events: none;
    z-index: 1;
    border-radius: 1px;
}
.mf::after {
    content: '';
    position: absolute;
    inset: 5px;
    border: 1px solid var(--gold-champagne);
    opacity: 0.9;
    pointer-events: none;
    z-index: 3;
    border-radius: 1px;
}
.mf img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
    position: relative;
    z-index: 2;
    border: 1px solid rgba(201,168,108,0.28);
    box-shadow: inset 0 0 0 3px #ffffff;
    border-radius: 1px;
}
.mf .cap {
    margin-top: 12px;
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 14px;
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
.mf .cap::before {
    content: '\2766';
    position: absolute;
    top: -9px; left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(160deg, var(--marble-white), var(--marble-ice));
    color: var(--gold);
    font-size: 12px;
    padding: 0 10px;
    line-height: 1;
}

.mf.sway { animation: mf-sway 9s ease-in-out infinite; }
@keyframes mf-sway {
    0%, 100% { transform: rotate(var(--rot, -1deg)) translateY(0); }
    50% { transform: rotate(calc(var(--rot, -1deg) + 0.5deg)) translateY(-3px); }
}
.mf.lift { transition: transform 0.3s ease; }
.mf.lift:active { transform: translateY(-2px) scale(1.01); }

.smf {
    position: absolute;
    z-index: 2;
    opacity: 0.72;
    pointer-events: none;
    background: linear-gradient(160deg, #fff, #f5f7fa, #eef1f6);
    padding: 4px;
    border: 1px solid var(--gold-champagne);
    box-shadow: inset 0 0 0 1px #fff, 0 2px 6px var(--shadow-soft), 0 0 8px var(--shadow-gold);
    border-radius: 1px;
}
.smf img { display: block; width: 100%; height: auto; border: 1px solid rgba(201,168,108,0.25); }

/* TYPOGRAPHY */
.big-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(48px, 14vw, 84px);
    background: linear-gradient(145deg, var(--gold-deep) 0%, var(--gold) 45%, var(--gold-bright) 70%, var(--gold-soft) 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 8px;
    z-index: 100;
    position: relative;
    text-shadow: 0 2px 12px rgba(201, 168, 108, 0.20);
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 8vw, 42px);
    font-weight: 600;
    font-style: italic;
    color: var(--ink);
    letter-spacing: 0.01em;
    margin-bottom: 6px;
    text-align: center;
    z-index: 100;
    position: relative;
}
.section-sub {
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    font-weight: 500;
    color: var(--ink-soft);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 18px;
    z-index: 100;
    position: relative;
}
.divider {
    width: 80px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 14px auto 18px;
    position: relative;
    z-index: 100;
}
.divider::before {
    content: '\2766';
    position: absolute;
    top: -10px; left: 50%;
    transform: translateX(-50%);
    color: var(--gold);
    font-size: 13px;
    padding: 0 10px;
}

.body-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: 17px;
    line-height: 1.9;
    color: var(--ink);
    font-weight: 500;
    text-align: center;
    max-width: 460px;
    z-index: 100;
}
.body-text p { margin-bottom: 12px; }

.spacer-s { height: 10px; }
.spacer-m { height: 18px; }
.spacer-l { height: 28px; }
.center-x { display: flex; flex-direction: column; align-items: center; width: 100%; }

/* ============ PAGE 1 – PORTAL OPENING ============ */
.portal-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    padding: 20px;
    gap: 28px;
}

.portal-arch {
    position: relative;
    width: min(280px, 74vw);
    aspect-ratio: 1 / 1.3;
    perspective: 1200px;
}
.arch-shape {
    position: absolute;
    inset: 0;
    background: linear-gradient(160deg, var(--marble-white), var(--marble-cloud));
    border-radius: 50% 50% 8px 8px / 38% 38% 8px 8px;
    box-shadow:
        inset 0 0 0 2px var(--gold-champagne),
        inset 0 0 0 8px var(--marble-ice),
        inset 0 0 0 10px var(--gold),
        0 6px 22px var(--shadow-medium),
        0 0 32px var(--shadow-gold);
}
.arch-shape::before {
    content: '';
    position: absolute;
    inset: 14px;
    border-radius: 48% 48% 6px 6px / 36% 36% 6px 6px;
    background:
        radial-gradient(ellipse at 50% 25%, rgba(255,255,255,0.95) 0%, rgba(245,247,250,0.88) 40%, rgba(238,241,246,0.94) 100%),
        url("@BG_SITE@");
    background-size: cover;
    background-position: center;
    box-shadow:
        inset 0 0 40px rgba(201,168,108,0.22),
        inset 0 0 0 1px var(--gold-champagne);
}
.arch-shape::after {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 520' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='pv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.22 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23pv)'/%3E%3C/svg%3E");
    background-size: cover;
    mix-blend-mode: multiply;
    opacity: 0.9;
    border-radius: 50% 50% 8px 8px / 38% 38% 8px 8px;
    pointer-events: none;
}

.arch-glow {
    position: absolute;
    left: 16%;
    right: 16%;
    top: 20%;
    bottom: 10%;
    background: radial-gradient(ellipse at 50% 50%, rgba(243,230,196,0.65), rgba(233,217,180,0.25) 50%, transparent 75%);
    filter: blur(6px);
    animation: portal-glow 3.4s ease-in-out infinite;
    z-index: 2;
}
@keyframes portal-glow {
    0%, 100% { opacity: 0.55; transform: scale(1); }
    50% { opacity: 0.95; transform: scale(1.05); }
}

.arch-rays {
    position: absolute;
    inset: 0;
    background:
        conic-gradient(from 270deg at 50% 30%, transparent 0deg, rgba(243,230,196,0.12) 10deg, transparent 22deg,
                     rgba(243,230,196,0.10) 34deg, transparent 46deg, rgba(243,230,196,0.14) 60deg, transparent 72deg,
                     rgba(243,230,196,0.09) 86deg, transparent 98deg, rgba(243,230,196,0.11) 112deg, transparent 124deg,
                     rgba(243,230,196,0.13) 140deg, transparent 152deg, rgba(243,230,196,0.10) 166deg, transparent 180deg);
    mix-blend-mode: screen;
    animation: portal-rays 9s linear infinite;
    z-index: 3;
}
@keyframes portal-rays {
    0% { transform: rotate(0deg); opacity: 0.8; }
    100% { transform: rotate(360deg); opacity: 0.8; }
}

.arch-title {
    position: absolute;
    left: 0; right: 0;
    top: 22%;
    display: flex; flex-direction: column; align-items: center;
    z-index: 4;
    gap: 4px;
    pointer-events: none;
}
.arch-title .k {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    letter-spacing: 0.3em;
    color: var(--gold-deep);
}
.arch-title .a {
    font-family: 'Dancing Script', cursive;
    font-size: 42px;
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    line-height: 1;
}
.arch-title .amp {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    color: var(--gold-deep);
    opacity: 0.75;
}

.portal-sub {
    font-family: 'Cormorant Garamond', serif;
    letter-spacing: 0.26em;
    text-transform: uppercase;
    color: var(--ink-soft);
    font-size: 13px;
    text-align: center;
    z-index: 100;
}

.enter-btn {
    margin-top: 4px;
    background: linear-gradient(160deg, var(--marble-white), var(--marble-cloud));
    color: var(--gold-deep);
    border: 1px solid var(--gold-champagne);
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    padding: 16px 36px;
    cursor: pointer;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold-champagne),
        0 6px 20px var(--shadow-medium),
        0 0 18px var(--shadow-gold);
    border-radius: 2px;
    transition: transform 0.25s ease, box-shadow 0.25s ease, background 0.25s ease;
    min-height: 52px;
    position: relative;
    z-index: 100;
}
.enter-btn::after {
    content: '';
    position: absolute;
    inset: 6px;
    border: 1px solid var(--gold);
    opacity: 0.75;
    pointer-events: none;
    border-radius: 1px;
}
.enter-btn:hover { background: linear-gradient(160deg, var(--marble-cloud), var(--marble-ice)); }
.enter-btn:active {
    transform: translateY(2px) scale(0.97);
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold),
        0 2px 8px var(--shadow-medium);
}

.portal-open .arch-shape { animation: portal-open 1.4s cubic-bezier(0.22, 0.8, 0.30, 1) forwards; }
.portal-open .arch-glow { animation: portal-burst 1.2s ease-out forwards; }
.portal-open .arch-rays { animation-play-state: paused; opacity: 0; transition: opacity 0.6s; }
@keyframes portal-open {
    0% { transform: scale(1); opacity: 1; }
    40% { transform: scale(1.08); opacity: 1; filter: brightness(1.4); }
    100% { transform: scale(2.6); opacity: 0; filter: brightness(1.8) blur(6px); }
}
@keyframes portal-burst {
    0% { opacity: 0.6; transform: scale(1); filter: blur(6px); }
    50% { opacity: 1; transform: scale(1.4); filter: blur(10px); }
    100% { opacity: 0; transform: scale(3); filter: blur(16px); }
}

/* ============ PAGE 2 – INTRO ============ */
.intro-wrap {
    width: 100%;
    max-width: 460px;
    display: flex; flex-direction: column; align-items: center;
    gap: 14px;
    padding: 8px 4px 0;
}
.intro-names {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(40px, 11vw, 64px);
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    line-height: 1;
    text-align: center;
}
.intro-meta {
    font-family: 'Playfair Display', serif;
    font-size: 14px;
    letter-spacing: 0.35em;
    color: var(--gold-deep);
    text-transform: uppercase;
    text-align: center;
    font-weight: 700;
}
.intro-para {
    font-family: 'Cormorant Garamond', serif;
    font-size: 17px;
    line-height: 1.95;
    color: var(--ink);
    text-align: center;
    font-weight: 500;
    font-style: italic;
    margin-top: 6px;
}

/* ============ PAGE 3 – TIMELINE (moments 1..4) ============ */
.tl-wrap {
    width: 100%;
    max-width: 460px;
    position: relative;
    z-index: 100;
    padding: 6px 0 0;
}
.tl-moments {
    display: flex;
    flex-direction: column;
    gap: 14px;
    width: 100%;
}
.tl-row {
    display: flex;
    gap: 14px;
    align-items: center;
    width: 100%;
}
.tl-row:nth-child(even) { flex-direction: row-reverse; }
.tl-photo {
    flex: 0 0 46%;
    max-width: 46%;
}
.tl-photo .mf { padding: 10px; }
.tl-photo .mf img { aspect-ratio: 4 / 5; object-fit: cover; }
.tl-card {
    flex: 1;
    min-width: 0;
    background: linear-gradient(160deg, var(--marble-white), var(--marble-ice) 60%, var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    padding: 16px 14px;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold-champagne),
        0 4px 12px var(--shadow-medium),
        0 0 14px var(--shadow-gold);
    border-radius: 2px;
    position: relative;
}
.tl-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='tv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.08 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23tv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
    z-index: 1;
}
.tl-card > * { position: relative; z-index: 2; }
.tl-num {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.3em;
    color: var(--gold-deep);
    text-transform: uppercase;
}
.tl-date {
    font-family: 'Caveat', cursive;
    font-size: 18px;
    font-weight: 600;
    color: var(--gold-deep);
    margin: 2px 0 6px;
}
.tl-title {
    font-family: 'Playfair Display', serif;
    font-size: 17px;
    font-weight: 700;
    color: var(--ink);
    margin-bottom: 4px;
    line-height: 1.25;
}
.tl-note {
    font-family: 'Cormorant Garamond', serif;
    font-size: 14px;
    line-height: 1.6;
    color: var(--ink-soft);
    font-style: italic;
    font-weight: 500;
}

.tl-spine {
    position: absolute;
    left: 50%;
    top: 40px;
    bottom: 40px;
    width: 2px;
    margin-left: -1px;
    background: linear-gradient(180deg,
        transparent 0%,
        var(--gold-champagne) 8%,
        var(--gold) 50%,
        var(--gold-champagne) 92%,
        transparent 100%);
    opacity: 0.75;
    z-index: 1;
    box-shadow: 0 0 6px var(--shadow-gold);
}
.tl-spine::before,
.tl-spine::after {
    content: '';
    position: absolute;
    left: -5px;
    width: 12px; height: 12px; border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, var(--gold-light), var(--gold) 60%, var(--gold-deep));
    border: 2px solid var(--marble-white);
    box-shadow: 0 0 0 1px var(--gold-champagne), 0 0 8px var(--shadow-gold);
}
.tl-spine::before { top: 0; }
.tl-spine::after { bottom: 0; }

/* ============ PAGE 4 – ASTROLOGY ============ */
.ast-wrap {
    width: 100%;
    max-width: 460px;
    position: relative;
    z-index: 100;
}
.ast-stage {
    position: relative;
    width: 100%;
    aspect-ratio: 4 / 5;
    margin: 6px auto 0;
}
.ast-stars {
    position: absolute;
    inset: -6%;
    background-image: url("@STARS@");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    mix-blend-mode: screen;
    opacity: 0.9;
    z-index: 5;
    pointer-events: none;
    filter: drop-shadow(0 0 4px rgba(243,230,196,0.6));
    animation: stars-twinkle 4s ease-in-out infinite;
}
@keyframes stars-twinkle {
    0%, 100% { opacity: 0.75; }
    50% { opacity: 1; }
}
.ast-center {
    position: absolute;
    left: 50%;
    bottom: 4%;
    transform: translateX(-50%);
    width: 42%;
    z-index: 4;
}
.ast-center .mf { padding: 10px; border-radius: 50%; }
.ast-center .mf::before, .ast-center .mf::after { border-radius: 50%; }
.ast-center .mf img { border-radius: 50% !important; aspect-ratio: 1/1; object-fit: cover; }
.ast-center .mf .cap { border: none; padding: 6px 0 0; }

.ast-moons {
    position: absolute;
    top: 0;
    left: 0; right: 0;
    height: 62%;
    z-index: 3;
}
.ast-moon {
    position: absolute;
    top: 4%;
    width: 38%;
}
.ast-moon.left { left: 0; }
.ast-moon.right { right: 0; }
.ast-moon .mf { padding: 10px; border-radius: 50%; }
.ast-moon .mf::before, .ast-moon .mf::after { border-radius: 50%; }
.ast-moon .mf img { aspect-ratio: 1/1; object-fit: cover; border-radius: 50% !important; }

.ast-names {
    position: absolute;
    left: 0; right: 0; top: 54%;
    display: flex;
    justify-content: space-between;
    font-family: 'Playfair Display', serif;
    font-size: 12px;
    letter-spacing: 0.24em;
    color: var(--gold-deep);
    text-transform: uppercase;
    z-index: 6;
    padding: 0 2%;
}
.ast-center-label {
    position: absolute;
    left: 50%;
    top: 62%;
    transform: translateX(-50%);
    font-family: 'Playfair Display', serif;
    font-size: 12px;
    letter-spacing: 0.24em;
    color: var(--gold-deep);
    text-transform: uppercase;
    white-space: nowrap;
    z-index: 6;
}
.ast-legend {
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    line-height: 1.75;
    color: var(--ink-soft);
    font-style: italic;
    margin-top: 12px;
    max-width: 420px;
}

/* ============ PAGE 5 – ME 1..10 ============ */
.me-grid {
    width: 100%;
    max-width: 460px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    z-index: 100;
    margin-top: 6px;
}
.me-grid .me { min-width: 0; }
.me-grid .me .mf {
    display: block;
    padding: 5px;
    box-shadow:
        inset 0 0 0 1px var(--gold-light),
        0 2px 5px var(--shadow-soft),
        0 6px 14px var(--shadow-medium),
        0 0 8px var(--shadow-gold);
}
.me-grid .me .mf::before { inset: 4px; }
.me-grid .me .mf::after { inset: 3px; }
.me-grid .me .mf img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    aspect-ratio: 3 / 4;
}
.me-grid .me.span2 { grid-column: span 2; }
.me-grid .me.span2 .mf img { aspect-ratio: 16 / 10; }

/* ============ PAGE 6 – DEAR AYA LETTER with letter.jfif frame ============ */
.letter-wrap {
    position: relative;
    width: 100%;
    max-width: 460px;
    z-index: 100;
}
.letter-frame {
    position: relative;
    width: 100%;
    margin: 4px auto 0;
}
.letter-frame .bg-img {
    display: block;
    width: 100%;
    height: auto;
    opacity: 0.95;
    border-radius: 2px;
    filter: contrast(1.02) saturate(1.02);
}
.letter-text {
    position: absolute;
    inset: 11% 12% 13%;
    overflow-y: auto;
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(12px, 3.4vw, 16px);
    line-height: 1.7;
    color: #3a2a1e;
    font-weight: 500;
    padding-right: 4px;
}
.letter-text::-webkit-scrollbar { width: 3px; }
.letter-text::-webkit-scrollbar-thumb { background: rgba(201,168,108,0.4); border-radius: 3px; }
.letter-text p { margin-bottom: 0.7em; }
.letter-text .sal {
    font-family: 'Dancing Script', cursive;
    font-size: 1.35em;
    color: var(--gold-deep);
    margin-bottom: 0.4em;
}
.letter-text .sig {
    font-family: 'Dancing Script', cursive;
    font-size: 1.5em;
    color: var(--gold-deep);
    text-align: right;
    margin-top: 0.8em;
}

/* ============ PAGE 7 – US IN NUMBERS ============ */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    width: 100%;
    max-width: 460px;
    margin-top: 6px;
    z-index: 100;
}
.stat-card {
    background: linear-gradient(160deg, var(--marble-white) 0%, var(--marble-ice) 50%, var(--marble-cloud) 100%);
    border: 1px solid var(--gold-champagne);
    padding: 20px 10px 18px;
    text-align: center;
    position: relative;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        inset 0 0 0 2px var(--gold-champagne),
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
.stat-card > * { position: relative; z-index: 2; }
.stat-ico {
    font-size: 22px;
    margin-bottom: 4px;
    color: var(--gold-deep);
}
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: clamp(26px, 8vw, 34px);
    font-weight: 700;
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    line-height: 1.1;
    margin-bottom: 4px;
}
.stat-label {
    font-family: 'Caveat', cursive;
    font-size: 16px;
    font-weight: 500;
    color: var(--ink-soft);
    line-height: 1.2;
}

/* ============ PAGE 8 – 12 THINGS ============ */
.twelves {
    width: 100%;
    max-width: 460px;
    margin-top: 6px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 100;
}
.twelve {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    padding: 12px 12px 12px 14px;
    background: linear-gradient(160deg, var(--marble-white), var(--marble-ice) 60%, var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    border-radius: 2px;
    box-shadow:
        inset 0 0 0 1px var(--marble-white),
        0 2px 6px var(--shadow-soft),
        0 6px 16px var(--shadow-medium),
        0 0 10px var(--shadow-gold);
    position: relative;
}
.twelve::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='twv'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.82  0 0 0 0 0.76  0 0 0 0 0.64  0 0 0 0.08 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23twv)'/%3E%3C/svg%3E");
    background-size: cover;
    opacity: 0.9;
    pointer-events: none;
    z-index: 1;
}
.twelve > * { position: relative; z-index: 2; }
.twelve-num {
    flex: 0 0 auto;
    width: 40px; height: 40px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    background: radial-gradient(circle at 30% 30%, var(--gold-light), var(--gold) 60%, var(--gold-deep));
    color: var(--marble-white);
    font-family: 'Playfair Display', serif;
    font-size: 15px; font-weight: 700;
    box-shadow: 0 0 0 2px var(--marble-white), 0 0 0 3px var(--gold-champagne), 0 0 8px var(--shadow-gold);
}
.twelve-month {
    font-family: 'Playfair Display', serif;
    font-size: 12px;
    letter-spacing: 0.28em;
    color: var(--gold-deep);
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 2px;
}
.twelve-body {
    font-family: 'Cormorant Garamond', serif;
    font-size: 15px;
    line-height: 1.6;
    color: var(--ink);
    font-weight: 500;
}

/* ============ PAGE 9 – OUR GIFTS ============ */
.gifts-wrap {
    width: 100%;
    max-width: 460px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 18px;
    margin-top: 6px;
    z-index: 100;
}
.gifts-top {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    width: 100%;
}
.gift-card {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
}
.gift-card .mf img { aspect-ratio: 4 / 5; object-fit: cover; }
.gift-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 12px;
    letter-spacing: 0.24em;
    color: var(--gold-deep);
    text-transform: uppercase;
    font-weight: 700;
}
.gifts-divider {
    width: 80%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold-champagne), transparent);
    margin: 2px auto;
    position: relative;
}
.gifts-divider::before {
    content: '\2726';
    position: absolute;
    top: -10px; left: 50%;
    transform: translateX(-50%);
    color: var(--gold);
    font-size: 15px;
    padding: 0 10px;
}
.gifts-center {
    width: 72%;
}
.gifts-center .mf img { aspect-ratio: 4 / 5; object-fit: cover; }

/* ============ PAGE 10 – ENDING ============ */
.thanks-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 460px;
    padding: 8px 4px 0;
    gap: 14px;
}
.thanks-heart {
    font-size: 52px;
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 2px 8px rgba(201,168,108,0.35));
    animation: heart-beat 1.6s ease-in-out infinite;
}
@keyframes heart-beat {
    0%, 100% { transform: scale(1); }
    25% { transform: scale(1.08); }
    40% { transform: scale(0.98); }
    60% { transform: scale(1.06); }
    80% { transform: scale(1); }
}
.thanks-msg {
    font-family: 'Cormorant Garamond', serif;
    font-size: 18px;
    line-height: 1.95;
    color: var(--ink);
    text-align: center;
    font-style: italic;
    font-weight: 500;
}
.thanks-msg p { margin-bottom: 12px; }
.thanks-chapter {
    margin-top: 12px;
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 8vw, 42px);
    font-style: italic;
    font-weight: 600;
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    letter-spacing: 0.02em;
}
.thanks-ornament {
    width: 160px; height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 4px auto;
}
body.fade-out {
    transition: opacity 4s ease-out;
    opacity: 0;
}

/* Flower note pop-up */
.flower-note {
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
}
.flower-note.show {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
    pointer-events: all;
}
.flower-note::before {
    content: '\2766';
    display: block;
    font-size: 16px;
    background: linear-gradient(145deg, var(--gold-deep), var(--gold-bright));
    -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
}
.fn-close {
    margin-top: 14px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold-deep);
    cursor: pointer;
    display: inline-block;
    padding: 4px 14px;
    background: linear-gradient(145deg, var(--marble-white), var(--marble-cloud));
    border: 1px solid var(--gold-champagne);
    border-radius: 1px;
    box-shadow: 0 2px 6px var(--shadow-soft);
}

/* RESPONSIVE */
@media (max-width: 380px) {
    .page { padding: 68px 18px 112px; }
    .big-title { font-size: clamp(40px, 13vw, 52px); }
    .section-title { font-size: clamp(24px, 7.8vw, 32px); }
    .stats-grid { gap: 10px; }
    .stat-card { padding: 16px 8px 14px; }
    .nav-btn { padding: 10px 14px; font-size: 12px; min-height: 42px; }
    #btn-prev { left: 10px; }
    #btn-next { right: 10px; }
    .ast-names { font-size: 11px; letter-spacing: 0.18em; }
    .me-grid { gap: 6px; }
    .me-grid .me .mf { padding: 4px; }
    .letter-text { inset: 10% 10% 12%; font-size: clamp(11px, 3.3vw, 14px); }
    .portal-arch { width: 68vw; }
}
@media (min-width: 500px) {
    .page { padding: 64px 28px 120px; }
    .intro-wrap, .tl-wrap, .ast-wrap, .stats-grid, .gifts-wrap, .letter-wrap, .me-grid, .thanks-wrap, .twelves { max-width: 460px; }
}
@media (min-width: 800px) {
    #page-dots { gap: 7px; }
    .pdot { width: 7px; height: 7px; }
}
</style>
</head>
<body>

<div class="vignette"></div>
<div class="corridor-fade top"></div>
<div class="corridor-fade bottom"></div>
<div class="flower-note" id="flower-note">
    <span id="flower-note-text">Every memory in these halls was laid for you.</span>
    <div class="fn-close" onclick="closeFlowerNote()">close</div>
</div>

<audio id="bg-music" loop preload="auto">
    <source src="@MUSIC@" type="audio/mpeg">
</audio>

<div id="music-bar">
    <span class="music-track"><span class="note">♪</span> never coming back</span>
    <div class="music-controls">
        <input type="range" id="volume-slider" min="0" max="1" step="0.05" value="0.55">
        <div id="music-toggle" title="Play / Pause">🔇</div>
    </div>
</div>

<div id="home-btn" title="Portal">⌂</div>

<div id="pages-wrap">
<div id="pages">

<!-- =============== PAGE 1 – PORTAL OPENING =============== -->
<div class="page active" id="p0">
    <div class="portal-wrap" id="portal-wrap">
        <div class="portal-arch" id="portal-arch">
            <div class="arch-shape"></div>
            <div class="arch-glow"></div>
            <div class="arch-rays"></div>
            <div class="arch-title">
                <div class="k">KARIM</div>
                <div class="amp">&amp;</div>
                <div class="a">Aya</div>
            </div>
        </div>
        <div class="portal-sub">a mausoleum of memories · ten chambers</div>
        <button class="enter-btn" id="enter-btn">Step Inside</button>
    </div>
</div>

<!-- =============== PAGE 2 – INTRO =============== -->
<div class="page" id="p1">
    <div class="center-x">
        <div class="intro-wrap">
            <div class="intro-meta">from the first hello</div>
            <div class="divider"></div>
            <div class="intro-names">Karim &amp; Aya</div>
            <div class="intro-meta" style="margin-top:10px; letter-spacing:0.22em; color: var(--ink-faint); font-weight:500;">29 · 07 · 2025 — forever onward</div>
            <div class="divider"></div>
            <div class="intro-para">
                I built these halls because one page could never hold you.
                Walk with me through every chamber, every moment, every moon
                that brought us here. Nothing here is random — every marble,
                every inscription, every photograph was placed for you.
                You are the reason every step forward feels like coming home.
            </div>
            <div class="spacer-m"></div>
            <div style="font-family:'Dancing Script', cursive; font-size:30px; background:linear-gradient(145deg,var(--gold-deep),var(--gold-bright)); -webkit-background-clip:text; background-clip:text; color:transparent; -webkit-text-fill-color:transparent;">
                for the girl who changed my sky.
            </div>
        </div>
    </div>
</div>

<!-- =============== PAGE 3 – TIMELINE 1..4 =============== -->
<div class="page" id="p2">
    <div class="center-x">
        <div class="section-title">A Year, In Stone</div>
        <div class="section-sub">four moments, four chambers</div>
        <div class="divider"></div>
        <div class="tl-wrap">
            <div class="tl-spine"></div>
            <div class="tl-moments">
                <div class="tl-row">
                    <div class="tl-photo"><div class="mf lift"><img loading="lazy" src="@M1@" alt="moment one"><div class="cap">I</div></div></div>
                    <div class="tl-card">
                        <div class="tl-num">Chamber I</div>
                        <div class="tl-date">29 · 07 · 2025</div>
                        <div class="tl-title">The Night We Met</div>
                        <div class="tl-note">You walked in and every hour I had lived before felt like a waiting room. I still remember what you were wearing. I always will.</div>
                    </div>
                </div>
                <div class="tl-row">
                    <div class="tl-photo"><div class="mf lift"><img loading="lazy" src="@M2@" alt="moment two"><div class="cap">II</div></div></div>
                    <div class="tl-card">
                        <div class="tl-num">Chamber II</div>
                        <div class="tl-date">the first week</div>
                        <div class="tl-title">When I Knew I Wouldn't Let Go</div>
                        <div class="tl-note">Four days in and I was already guarding conversations like relics. You smiled once and I mentally carved it into marble.</div>
                    </div>
                </div>
                <div class="tl-row">
                    <div class="tl-photo"><div class="mf lift"><img loading="lazy" src="@M3@" alt="moment three"><div class="cap">III</div></div></div>
                    <div class="tl-card">
                        <div class="tl-num">Chamber III</div>
                        <div class="tl-date">our first</div>
                        <div class="tl-title">The Day It Became Real</div>
                        <div class="tl-note">The first time we said it out loud. The first time our hands fit. The first of ten thousand firsts I intend to have with you.</div>
                    </div>
                </div>
                <div class="tl-row">
                    <div class="tl-photo"><div class="mf lift"><img loading="lazy" src="@M4@" alt="moment four"><div class="cap">IV</div></div></div>
                    <div class="tl-card">
                        <div class="tl-num">Chamber IV</div>
                        <div class="tl-date">today</div>
                        <div class="tl-title">This Mausoleum, For You</div>
                        <div class="tl-note">A whole year of us. I didn't know love could be this quiet, this sure, this constant. So I built it in stone.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- =============== PAGE 4 – ASTROLOGY =============== -->
<div class="page" id="p3">
    <div class="center-x">
        <div class="section-title">Written in the Sky</div>
        <div class="section-sub">before us, the stars agreed</div>
        <div class="divider"></div>
        <div class="ast-wrap">
            <div class="ast-stage">
                <div class="ast-stars"></div>
                <div class="ast-moons">
                    <div class="ast-moon left"><div class="mf sway" style="--rot:-2deg;"><img loading="lazy" src="@K_BDAY@" alt="karim moon"></div></div>
                    <div class="ast-moon right"><div class="mf sway" style="--rot:2deg;"><img loading="lazy" src="@A_BDAY@" alt="aya moon"></div></div>
                </div>
                <div class="ast-names">
                    <span>Karim</span>
                    <span>Aya</span>
                </div>
                <div class="ast-center"><div class="mf sway" style="--rot:0deg;"><img loading="lazy" src="@MEET@" alt="the night we met"></div></div>
                <div class="ast-center-label">our sky</div>
            </div>
            <div class="ast-legend">
                Your moon, my moon, and the exact night they finally shared the same sky.
                I looked up the constellations above us on 29 · 07 · 2025 —
                every star, every line, every faint distant sun
                was already arranging itself for us.
            </div>
        </div>
    </div>
</div>

<!-- =============== PAGE 5 – SOME PHOTOS OF ME =============== -->
<div class="page" id="p4">
    <div class="center-x">
        <div class="section-title">Some Photos of Me</div>
        <div class="section-sub">for when you miss my face</div>
        <div class="divider"></div>
        <div class="me-grid" id="me-grid">
            <div class="me span2"><div class="mf lift"><img loading="lazy" src="@ME1@" alt="me 1"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME2@" alt="me 2"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME3@" alt="me 3"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME4@" alt="me 4"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME5@" alt="me 5"></div></div>
            <div class="me span2"><div class="mf lift"><img loading="lazy" src="@ME6@" alt="me 6"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME7@" alt="me 7"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME8@" alt="me 8"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME9@" alt="me 9"></div></div>
            <div class="me"><div class="mf lift"><img loading="lazy" src="@ME10@" alt="me 10"></div></div>
        </div>
        <div class="spacer-s"></div>
        <div style="font-family:'Caveat', cursive; font-size:19px; color:var(--gold-deep); text-align:center; z-index:100;">
            ten versions of the boy who belongs to you.
        </div>
    </div>
</div>

<!-- =============== PAGE 6 – DEAR AYA LETTER =============== -->
<div class="page" id="p5">
    <div class="center-x">
        <div class="section-title">Dear Aya</div>
        <div class="section-sub">written in stone, sealed in gold</div>
        <div class="divider"></div>
        <div class="letter-wrap">
            <div class="letter-frame">
                <img class="bg-img" src="@LETTER@" alt="letter frame">
                <div class="letter-text">
                    <div class="sal">My love,</div>
                    <p>If I tried to put every version of loving you into words, I would run out of alphabet. You are the first good morning I look forward to and the last goodnight I never want to end.</p>
                    <p>You have made softer every corner of me that used to be sharp. You have made patient every hour I used to rush. You have taught me that home is not a place — it is a girl who says your name like she's saying a prayer.</p>
                    <p>I built every chamber of this place thinking of how you would look at each one. I thought about you reading this, years from now, older, holding my hand, and I hope by then I will have told you everything a thousand times over.</p>
                    <p>You are my favourite story, my quietest cathedral, my most certain thing. Whatever comes next, I meet it with you.</p>
                    <p>With all I am,<br>all I ever will be,</p>
                    <div class="sig">Yours, always — Karim</div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- =============== PAGE 7 – US IN NUMBERS =============== -->
<div class="page" id="p6">
    <div class="center-x">
        <div class="section-title">Us, In Numbers</div>
        <div class="section-sub">the arithmetic of loving you</div>
        <div class="divider"></div>
        <div class="stats-grid">
            <div class="stat-card"><div class="stat-ico">🗓️</div><div class="stat-num">365</div><div class="stat-label">days together</div></div>
            <div class="stat-card"><div class="stat-ico">☾</div><div class="stat-num">∞</div><div class="stat-label">moons together</div></div>
            <div class="stat-card"><div class="stat-ico">💕</div><div class="stat-num">5,280+</div><div class="stat-label">messages</div></div>
            <div class="stat-card"><div class="stat-ico">📞</div><div class="stat-num">248h</div><div class="stat-label">on call</div></div>
            <div class="stat-card"><div class="stat-ico">💐</div><div class="stat-num">12</div><div class="stat-label">bouquets</div></div>
            <div class="stat-card"><div class="stat-ico">🥂</div><div class="stat-num">27</div><div class="stat-label">our dates</div></div>
            <div class="stat-card"><div class="stat-ico">🎁</div><div class="stat-num">19</div><div class="stat-label">gifts exchanged</div></div>
            <div class="stat-card"><div class="stat-ico">📷</div><div class="stat-num">1,460+</div><div class="stat-label">photographs</div></div>
            <div class="stat-card"><div class="stat-ico">🚗</div><div class="stat-num">842</div><div class="stat-label">kilometres</div></div>
            <div class="stat-card"><div class="stat-ico">💌</div><div class="stat-num">∞</div><div class="stat-label">"I love you"s</div></div>
            <div class="stat-card"><div class="stat-ico">🌙</div><div class="stat-num">312</div><div class="stat-label">slept on call</div></div>
            <div class="stat-card"><div class="stat-ico">♾️</div><div class="stat-num">1</div><div class="stat-label">you, forever</div></div>
        </div>
    </div>
</div>

<!-- =============== PAGE 8 – 12 THINGS =============== -->
<div class="page" id="p7">
    <div class="center-x">
        <div class="section-title">Twelve Things</div>
        <div class="section-sub">one for each month we have carried each other</div>
        <div class="divider"></div>
        <div class="twelves">
            <div class="twelve"><div class="twelve-num">01</div><div><div class="twelve-month">Month One</div><div class="twelve-body">The way you said my name the first time — slow, like you were tasting it.</div></div></div>
            <div class="twelve"><div class="twelve-num">02</div><div><div class="twelve-month">Month Two</div><div class="twelve-body">How I started guarding every 'good morning' like it was a small relic.</div></div></div>
            <div class="twelve"><div class="twelve-num">03</div><div><div class="twelve-month">Month Three</div><div class="twelve-body">Your sleepy voice at 3 a.m. when you wake up just to say you miss me.</div></div></div>
            <div class="twelve"><div class="twelve-num">04</div><div><div class="twelve-month">Month Four</div><div class="twelve-body">The way you cry at movies and pretend you aren't crying — I know. I love it.</div></div></div>
            <div class="twelve"><div class="twelve-num">05</div><div><div class="twelve-month">Month Five</div><div class="twelve-body">How you save every photo, every voice note, every small thing like I do.</div></div></div>
            <div class="twelve"><div class="twelve-num">06</div><div><div class="twelve-month">Month Six</div><div class="twelve-body">The way you hold my hand tighter in crowds — a small, quiet promise.</div></div></div>
            <div class="twelve"><div class="twelve-num">07</div><div><div class="twelve-month">Month Seven</div><div class="twelve-body">Your laugh when something catches you completely off guard — it rearranges my whole day.</div></div></div>
            <div class="twelve"><div class="twelve-num">08</div><div><div class="twelve-month">Month Eight</div><div class="twelve-body">How proud you get of tiny, silly things I do — no one has ever believed in me like that.</div></div></div>
            <div class="twelve"><div class="twelve-num">09</div><div><div class="twelve-month">Month Nine</div><div class="twelve-body">The way you apologise softly and mean it — no games, no pride, just us.</div></div></div>
            <div class="twelve"><div class="twelve-num">10</div><div><div class="twelve-month">Month Ten</div><div class="twelve-body">How you already talk about our future like it's guaranteed — because for you, it will be.</div></div></div>
            <div class="twelve"><div class="twelve-num">11</div><div><div class="twelve-month">Month Eleven</div><div class="twelve-body">How you still get shy when I compliment you after all this time.</div></div></div>
            <div class="twelve"><div class="twelve-num">12</div><div><div class="twelve-month">Month Twelve</div><div class="twelve-body">All of it. Every part. You. In every season, every mood, every version — I love you twelve months deep and I'm only getting started.</div></div></div>
        </div>
    </div>
</div>

<!-- =============== PAGE 9 – OUR GIFTS =============== -->
<div class="page" id="p8">
    <div class="center-x">
        <div class="section-title">Our Gifts</div>
        <div class="section-sub">proof we were thinking of each other, always</div>
        <div class="divider"></div>
        <div class="gifts-wrap">
            <div class="gifts-top">
                <div class="gift-card">
                    <div class="mf lift"><img loading="lazy" src="@G1@" alt="gifts from her to me"></div>
                    <div class="gift-title">from you → to me</div>
                </div>
                <div class="gift-card">
                    <div class="mf lift"><img loading="lazy" src="@G2@" alt="gifts from me to her"></div>
                    <div class="gift-title">from me → to you</div>
                </div>
            </div>
            <div class="gifts-divider"></div>
            <div class="gifts-center">
                <div class="mf lift"><img loading="lazy" src="@OUR_GIFT@" alt="our gift to each other"></div>
                <div class="gift-title" style="margin-top:8px;">the gift we gave each other — us.</div>
            </div>
        </div>
    </div>
</div>

<!-- =============== PAGE 10 – ENDING =============== -->
<div class="page" id="p9">
    <div class="center-x">
        <div class="thanks-wrap">
            <div class="thanks-heart">♡</div>
            <div class="section-title" style="margin-bottom:0;">Thank You</div>
            <div class="thanks-ornament"></div>
            <div class="thanks-msg">
                <p>For every "I miss you," every long call, every argument we survived,
                every small and quiet way you chose me — thank you.</p>
                <p>Thank you for trusting me with all the soft parts of you.
                Thank you for every sunrise we spent on the phone together.
                Thank you for the way you say my name like a promise.</p>
                <p>This mausoleum will never be big enough for how I feel about you.
                But it's a beginning.</p>
            </div>
            <div class="thanks-ornament"></div>
            <div class="thanks-chapter">To Chapter Two.</div>
            <div style="font-family:'Dancing Script', cursive; font-size:26px; background:linear-gradient(145deg,var(--gold-deep),var(--gold-bright)); -webkit-background-clip:text; background-clip:text; color:transparent; -webkit-text-fill-color:transparent;">
                until the stones forget — yours.
            </div>
        </div>
    </div>
</div>

</div>
</div>

<button class="nav-btn hidden" id="btn-prev" onclick="changePage(-1)">Previous</button>
<button class="nav-btn hidden" id="btn-next" onclick="changePage(1)">Continue</button>
<div id="page-dots"></div>

<script>
// MAUSOLEUM NAVIGATION
const total = 10;
let cur = 0;
let isAnimating = false;
const pages = document.querySelectorAll('.page');
const dotsContainer = document.getElementById('page-dots');
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');
const homeBtn = document.getElementById('home-btn');

// BG (1..28) scattered marble frames
const BGS = @BGS_ARRAY@;
function scatterDeco() {
    pages.forEach((p, idx) => {
        if (idx === 0 || idx === 9) return;  // portal & ending keep clean
        const count = 6;
        for (let i = 0; i < count; i++) {
            const pic = BGS[Math.floor(Math.random() * BGS.length)];
            const d = document.createElement('div');
            d.className = 'smf';
            d.innerHTML = '<img loading="lazy" src="' + pic + '" alt="">';
            const w = 40 + Math.random() * 36;
            d.style.width = w + 'px';
            const side = Math.random() > 0.5 ? 'left' : 'right';
            const xPos = side === 'left' ? (Math.random() * 5) : (93 + Math.random() * 5);
            d.style.left = xPos + '%';
            d.style.top = (8 + Math.random() * 82) + '%';
            d.style.transform = 'rotate(' + (Math.random() * 26 - 13) + 'deg)';
            d.style.opacity = (0.48 + Math.random() * 0.22).toFixed(2);
            p.prepend(d);
        }
    });
}
scatterDeco();

// Dots
for (let i = 0; i < total; i++) {
    const d = document.createElement('div');
    d.className = 'pdot' + (i === 0 ? ' active' : '');
    d.onclick = (function(idx){ return function(){ goTo(idx); }; })(i);
    dotsContainer.appendChild(d);
}
const dots = document.querySelectorAll('.pdot');

// MAUSOLEUM WALK-THROUGH transitions
function goTo(n) {
    if (isAnimating || n === cur) return;
    if (n < 0 || n >= total) return;
    isAnimating = true;
    const forward = n > cur;
    const oldPage = pages[cur];
    const newPage = pages[n];
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (reduced) {
        oldPage.classList.remove('active');
        newPage.classList.add('active');
        onPageChanged(n);
        isAnimating = false;
        return;
    }

    newPage.style.opacity = '0';
    newPage.scrollTop = 0;
    if (forward) {
        newPage.classList.add('entering-fwd');
        oldPage.classList.add('leaving-back');
    } else {
        newPage.classList.add('entering-back');
        oldPage.classList.add('leaving-fwd');
    }
    void newPage.offsetWidth;
    requestAnimationFrame(() => {
        newPage.style.opacity = '1';
        newPage.classList.add('active');
        newPage.classList.remove('entering-fwd', 'entering-back');
    });

    const cleanup = () => {
        oldPage.classList.remove('active', 'leaving-back', 'leaving-fwd');
        newPage.classList.remove('entering-fwd', 'entering-back');
        oldPage.style.opacity = '';
        newPage.style.opacity = '';
        onPageChanged(n);
        setTimeout(() => { isAnimating = false; }, 120);
    };
    setTimeout(cleanup, 1180);
}

function onPageChanged(n) {
    cur = n;
    dots.forEach((d, i) => d.classList.toggle('active', i === n));
    btnPrev.classList.toggle('hidden', n === 0);
    btnNext.classList.toggle('hidden', n === total - 1);
    homeBtn.classList.toggle('show', n !== 0);
    if (n === total - 1) {
        setTimeout(() => {
            document.body.classList.add('fade-out');
            fadeMusicOut();
        }, 2200);
    } else {
        document.body.classList.remove('fade-out');
    }
}

function changePage(dir) {
    const t = cur + dir;
    if (t < 0 || t >= total) return;
    goTo(t);
}

// Keyboard
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown') changePage(1);
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') changePage(-1);
    else if (e.key === 'Home') goTo(0);
});

// Swipe
let sx = 0, sy = 0, touching = false;
document.addEventListener('touchstart', (e) => {
    if (e.touches.length !== 1) return;
    sx = e.touches[0].clientX; sy = e.touches[0].clientY; touching = true;
}, {passive: true});
document.addEventListener('touchend', (e) => {
    if (!touching) return; touching = false;
    const t = e.changedTouches[0];
    const dx = t.clientX - sx; const dy = t.clientY - sy;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.2) {
        if (dx < 0) changePage(1);
        else changePage(-1);
    }
}, {passive: true});

// Home
homeBtn.addEventListener('click', () => goTo(0));

// MUSIC
const music = document.getElementById('bg-music');
const musicToggle = document.getElementById('music-toggle');
const volumeSlider = document.getElementById('volume-slider');
music.volume = parseFloat(volumeSlider.value);
let musicStarted = false;

function startMusic() {
    if (musicStarted) return;
    musicStarted = true;
    music.play().catch(() => {});
    musicToggle.textContent = '🔊';
}

function fadeMusicOut() {
    if (!musicStarted) return;
    const step = 0.010;
    const t = setInterval(() => {
        let v = parseFloat(music.volume);
        v = Math.max(0, v - step);
        music.volume = v;
        if (v <= 0) { clearInterval(t); music.pause(); }
    }, 150);
}

volumeSlider.addEventListener('input', (e) => {
    music.volume = parseFloat(e.target.value);
});
musicToggle.addEventListener('click', () => {
    if (!musicStarted) { startMusic(); return; }
    if (music.paused) { music.play().catch(()=>{}); musicToggle.textContent = '🔊'; }
    else { music.pause(); musicToggle.textContent = '🔇'; }
});

const firstInteract = () => {
    startMusic();
    document.removeEventListener('click', firstInteract);
    document.removeEventListener('touchstart', firstInteract);
};
document.addEventListener('click', firstInteract);
document.addEventListener('touchstart', firstInteract);

// PORTAL OPEN
const enterBtn = document.getElementById('enter-btn');
const portalWrap = document.getElementById('portal-wrap');
enterBtn.addEventListener('click', () => {
    startMusic();
    if (portalWrap) portalWrap.classList.add('portal-open');
    setTimeout(() => { goTo(1); }, 900);
});

// Easter egg: click constellation stars
function showFlowerNote(text) {
    const fn = document.getElementById('flower-note');
    document.getElementById('flower-note-text').textContent = text || 'Every stone here was laid for you.';
    fn.classList.add('show');
    setTimeout(() => closeFlowerNote(), 3800);
}
function closeFlowerNote() {
    document.getElementById('flower-note').classList.remove('show');
}
const starsEl = document.querySelector('.ast-stars');
if (starsEl) starsEl.addEventListener('click', () => showFlowerNote('The stars knew you before I did.'));
</script>
</body>
</html>
'''

# Apply placeholders
html = tpl
for k, v in placeholders.items():
    html = html.replace(k, v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

total = 10

print(f"Rebuilt index.html with {total} mausoleum pages.")
print(f"BG deco assets available: {len(BG_DECOS)}")
print(f"Music: {MUSIC}")
print(f"Me photos: {len(MES)}")
print(f"Moments: {len(MOMENTS)}")
print(f"Gifts: {len(GIFTS)}")
