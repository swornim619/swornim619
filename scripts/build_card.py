"""
build_card.py
=============
Regenerates assets/profile-card.svg (the terminal-style banner at the
top of the README).

HOW TO USE
----------
1. pip install pillow --break-system-packages
2. Edit the ITEMS list below to reflect your latest CV. Two entry types:
     ("kv", "Label", "Value", label_column_width)   -> a "Label: ..... Value" row
     ("section", "Title")                           -> a new "- Title ---" divider
   Also: ("blank",) for a spacer line, ("rule",) for a plain divider.
3. Put a fresh square-ish photo at scripts/photo.png if you want to
   regenerate the ASCII portrait too (optional - it only needs doing
   once, or whenever you want a new photo).
4. Run:  python3 build_card.py
5. Commit the updated assets/profile-card.svg.

No design decisions needed for small updates -- just add/edit rows in
ITEMS and re-run.
"""

import os
import html
from PIL import Image, ImageOps, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))
PHOTO_PATH = os.path.join(HERE, "photo.png")
OUT_SVG = os.path.join(HERE, "..", "assets", "profile-card.svg")

# ============================================================
# EDIT BELOW: this is the only section you should normally touch
# ============================================================
ITEMS = [
    ("plain", "swornim@sec-analyst", "GREEN", True),
    ("rule",),
    ("kv", "Role", "Cyber Security Analyst (VAPT)", 12),
    ("kv", "Focus", "Vulnerability Research & Disclosure", 12),
    ("kv", "Location", "Lalitpur, Nepal", 12),
    ("kv", "Education", "BSc(Hons) Ethical Hacking, Coventry Uni", 12),
    ("blank",),
    ("section", "Vulnerability Research"),
    ("kv", "Mozilla Firefox", "PDF.js URL-Spoof - Bugzilla #2025109", 18),
    ("kv", "Google / Guava", "BloomFilter DoS - OSS VRP Flagship", 18),
    ("kv", "OpenSSF Allstar", "Policy Bypass - GHSA-r4gf-cmfp-wq5c", 18),
    ("kv", "Elgg CMS", "Avatar Upload DoS - CVE-2026-65650", 18),
    # ADD-NEW-DISCLOSURE: copy a line above and edit it
    ("blank",),
    ("section", "Experience"),
    ("kv", "Cube Technologies", "Cyber Security Intern, VAPT", 20),
    ("kv", "Duration", "Jul 2025 - Dec 2025", 20),
    # ADD-NEW-JOB: copy the two lines above and edit them
    ("blank",),
    ("section", "Certifications"),
    ("kv", "Red Team", "CRTA, CRT Infra Dev, CRT Ops Mgmt", 15),
    ("kv", "API Security", "CASA, APIsec Certified Practitioner", 15),
    ("kv", "Compliance", "ISO/IEC 27001:2022 Lead Auditor", 15),
    # ADD-NEW-CERT: copy a line above and edit it
    ("blank",),
    ("section", "Contact"),
    ("kv", "Email", "swornimpoudel711@gmail.com", 10),
    ("kv", "LinkedIn", "swornim-poudel4a4721343", 10),
    ("kv", "GitHub", "swornim619", 10),
    ("kv", "Phone", "+977 9849782874", 10),
]
# ============================================================
# END EDIT ZONE
# ============================================================

COLORS = {
    "BG": "#0d1117",
    "BORDER": "#30363d",
    "GREEN": "#3fb950",
    "ORANGE": "#f0883e",
    "CYAN": "#79c0ff",
    "WHITE": "#e6edf3",
    "DIM": "#6e7681",
}

ART_COLS = 42
ART_ASPECT_CORRECTION = 0.55
ART_FONT = 15.5
ART_LH = 17.9
ART_CW = ART_FONT * 0.6
RAMP = " .:-=+*#%@$"

TEXT_FONT = 13
TEXT_LH = 18
CW = TEXT_FONT * 0.62
RULE_WIDTH_CH = 47
SECTION_WIDTH_CH = 47
PAD = 26
GAP = 34


def esc(s):
    return html.escape(s, quote=False)


def make_ascii_art(photo_path):
    img = Image.open(photo_path).convert("L")
    img = ImageOps.autocontrast(img, cutoff=1)
    img = ImageEnhance.Contrast(img).enhance(1.4)
    w, h = img.size
    new_w = ART_COLS
    new_h = round(ART_COLS * (h / w) * ART_ASPECT_CORRECTION)
    small = img.resize((new_w, new_h))
    pixels = list(small.getdata())
    lines = []
    for y in range(new_h):
        row = ""
        for x in range(new_w):
            p = pixels[y * new_w + x]
            idx = int(((255 - p) / 255) * (len(RAMP) - 1))
            row += RAMP[idx]
        lines.append(row)
    return lines


def art_color(ch):
    idx = RAMP.index(ch) if ch in RAMP else 0
    t = idx / (len(RAMP) - 1)
    lo, hi = (0x16, 0x4A, 0x5C), (0x5E, 0xEA, 0xD4)
    r = int(lo[0] + (hi[0] - lo[0]) * t)
    g = int(lo[1] + (hi[1] - lo[1]) * t)
    b = int(lo[2] + (hi[2] - lo[2]) * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def kv_line_len(label, value, lw):
    dots = max(2, lw - len(label))
    return len(label) + 1 + dots + 1 + len(value)


def build(art_lines, items):
    max_chars = 0
    for it in items:
        if it[0] == "kv":
            max_chars = max(max_chars, kv_line_len(it[1], it[2], it[3]))
        elif it[0] == "section":
            max_chars = max(max_chars, SECTION_WIDTH_CH)
        elif it[0] == "rule":
            max_chars = max(max_chars, RULE_WIDTH_CH)
        elif it[0] == "plain":
            max_chars = max(max_chars, len(it[1]))

    text_panel_w = max_chars * CW
    text_panel_h = len(items) * TEXT_LH
    art_panel_w = len(art_lines[0]) * ART_CW
    art_panel_h = len(art_lines) * ART_LH

    content_h = max(text_panel_h, art_panel_h)
    total_w = PAD + art_panel_w + GAP + text_panel_w + PAD
    total_h = PAD + content_h + PAD

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w:.0f}" height="{total_h:.0f}" '
             f'viewBox="0 0 {total_w:.0f} {total_h:.0f}">']
    parts.append('<defs><style>.mono{font-family:"SFMono-Regular",Consolas,'
                  '"Liberation Mono",Menlo,monospace;}</style></defs>')
    parts.append(f'<rect x="0" y="0" width="{total_w:.0f}" height="{total_h:.0f}" rx="14" '
                  f'fill="{COLORS["BG"]}" stroke="{COLORS["BORDER"]}" stroke-width="1.5"/>')

    art_y0 = PAD + (content_h - art_panel_h) / 2 + ART_FONT
    art_x0 = PAD
    parts.append(f'<g class="mono" font-size="{ART_FONT:.1f}">')
    for i, line in enumerate(art_lines):
        y = art_y0 + i * ART_LH
        tspans, j = [], 0
        while j < len(line):
            ch = line[j]
            k = j
            while k < len(line) and line[k] == ch:
                k += 1
            run = line[j:k]
            color = art_color(ch) if ch != " " else "none"
            tspans.append(f'<tspan fill="{color}">{esc(run)}</tspan>')
            j = k
        parts.append(f'<text x="{art_x0:.1f}" y="{y:.1f}" xml:space="preserve">{"".join(tspans)}</text>')
    parts.append("</g>")

    text_x0 = PAD + art_panel_w + GAP
    text_y0 = PAD + TEXT_FONT + max(0, (content_h - text_panel_h) / 2)
    parts.append(f'<g class="mono" font-size="{TEXT_FONT}">')
    for i, it in enumerate(items):
        y = text_y0 + i * TEXT_LH
        if it[0] == "blank":
            continue
        elif it[0] == "rule":
            parts.append(f'<text x="{text_x0:.1f}" y="{y:.1f}" fill="{COLORS["DIM"]}" '
                          f'xml:space="preserve">{esc("-" * RULE_WIDTH_CH)}</text>')
        elif it[0] == "plain":
            _, text, colorkey, bold = it
            weight = 'font-weight="700"' if bold else ""
            parts.append(f'<text x="{text_x0:.1f}" y="{y:.1f}" fill="{COLORS.get(colorkey, colorkey)}" '
                          f'{weight} xml:space="preserve">{esc(text)}</text>')
        elif it[0] == "section":
            title = it[1]
            left = f"- {title} "
            dashes = "-" * max(2, SECTION_WIDTH_CH - len(left))
            parts.append(
                f'<text x="{text_x0:.1f}" y="{y:.1f}" xml:space="preserve">'
                f'<tspan fill="{COLORS["ORANGE"]}" font-weight="700">- {esc(title)} </tspan>'
                f'<tspan fill="{COLORS["DIM"]}">{esc(dashes)}</tspan></text>'
            )
        elif it[0] == "kv":
            _, label, value, lw = it
            dots = max(2, lw - len(label))
            parts.append(
                f'<text x="{text_x0:.1f}" y="{y:.1f}" xml:space="preserve">'
                f'<tspan fill="{COLORS["CYAN"]}">{esc(label)}</tspan>'
                f'<tspan fill="{COLORS["DIM"]}">: {esc("." * dots)} </tspan>'
                f'<tspan fill="{COLORS["WHITE"]}">{esc(value)}</tspan></text>'
            )
    parts.append("</g></svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    art = make_ascii_art(PHOTO_PATH)
    svg = build(art, ITEMS)
    with open(OUT_SVG, "w") as f:
        f.write(svg)
    print(f"Wrote {os.path.abspath(OUT_SVG)}")
