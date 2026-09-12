"""
Genera las tarjetas "GitHub stats" y "Most used languages" del README como SVG,
usando la API de GitHub directamente (sin servicios externos ni límites de terceros).

Se ejecuta desde .github/workflows/stats.yml y escribe en dist/:
  stats-light.svg · stats-dark.svg · langs-light.svg · langs-dark.svg
"""
import json
import os
import urllib.request
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "JuanLesmes")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
HIDE_LANGS = {"TeX"}          # lenguajes que no se muestran
OUT = "dist"

PALETTE = {
    "light": dict(bg="#ffffff", title="#0f766e", text="#24292f", muted="#57606a", icon="#0ea5e9",
                  accent="#14b8a6", track="#e6fffb", border="#d0d7de"),
    "dark":  dict(bg="#0d1117", title="#2dd4bf", text="#c9d1d9", muted="#8b949e", icon="#22d3ee",
                  accent="#2dd4bf", track="#1b2a2a", border="#30363d"),
}
LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "C#": "#178600",
    "Java": "#b07219", "HTML": "#e34c26", "CSS": "#663399", "SCSS": "#c6538c", "Shell": "#89e051",
    "Dockerfile": "#384d54", "PowerShell": "#012456", "Jupyter Notebook": "#DA5B0B", "Kotlin": "#A97BFF",
    "Dart": "#00B4AB", "Rust": "#dea584", "C++": "#f34b7d", "C": "#555555", "Go": "#00ADD8",
    "PHP": "#4F5D95", "Ruby": "#701516", "Vue": "#41b883", "Svelte": "#ff3e00", "PLpgSQL": "#336790",
    "Makefile": "#427819", "Batchfile": "#C1F12E", "TeX": "#3D6117", "Swift": "#F05138",
}
FONT = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"


def api(path):
    req = urllib.request.Request("https://api.github.com" + path,
                                 headers={"Accept": "application/vnd.github+json",
                                          "User-Agent": "profile-stats-cards"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def search_total(query):
    try:
        return api(f"/search/{query}")["total_count"]
    except Exception as e:  # la búsqueda es lo primero que se limita; no tumbar todo por eso
        print("search failed:", query, e)
        return 0


def fmt(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)


# ---------------------------------------------------------------- datos
user = api(f"/users/{USER}")
repos = []
page = 1
while True:
    batch = api(f"/users/{USER}/repos?per_page=100&type=owner&page={page}")
    repos += batch
    if len(batch) < 100:
        break
    page += 1

own = [r for r in repos if not r.get("fork")]
stars = sum(r.get("stargazers_count", 0) for r in own)
commits = search_total(f"commits?q=author:{USER}")
prs = search_total(f"issues?q=author:{USER}+type:pr")
issues = search_total(f"issues?q=author:{USER}+type:issue")

lang_bytes = {}
for r in own:
    try:
        for lang, b in api(f"/repos/{USER}/{r['name']}/languages").items():
            if lang not in HIDE_LANGS:
                lang_bytes[lang] = lang_bytes.get(lang, 0) + b
    except Exception as e:
        print("languages failed:", r["name"], e)
total_bytes = sum(lang_bytes.values()) or 1
langs = sorted(lang_bytes.items(), key=lambda kv: kv[1], reverse=True)[:6]

# ---------------------------------------------------------------- iconos (trazos simples, 16x16)
ICONS = {
    "star": '<path d="M8 1.5l2 4.1 4.5.6-3.3 3.2.8 4.5L8 11.8 4 13.9l.8-4.5L1.5 6.2 6 5.6z" fill="none" stroke="{c}" stroke-width="1.4" stroke-linejoin="round"/>',
    "commit": '<circle cx="8" cy="8" r="3" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M0.5 8h4.5M11 8h4.5" stroke="{c}" stroke-width="1.6"/>',
    "pr": '<circle cx="4" cy="3.5" r="2" fill="none" stroke="{c}" stroke-width="1.4"/><circle cx="4" cy="12.5" r="2" fill="none" stroke="{c}" stroke-width="1.4"/><circle cx="12" cy="12.5" r="2" fill="none" stroke="{c}" stroke-width="1.4"/><path d="M4 5.5v5M12 10.5V7a2.5 2.5 0 0 0-2.5-2.5H8" fill="none" stroke="{c}" stroke-width="1.4"/>',
    "issue": '<circle cx="8" cy="8" r="6" fill="none" stroke="{c}" stroke-width="1.4"/><circle cx="8" cy="8" r="1.6" fill="{c}"/>',
    "people": '<circle cx="6" cy="5" r="2.6" fill="none" stroke="{c}" stroke-width="1.4"/><path d="M1.5 14c0-2.8 2-4.5 4.5-4.5S10.5 11.2 10.5 14" fill="none" stroke="{c}" stroke-width="1.4"/><path d="M11 6.5a2.2 2.2 0 1 0 0-4.4M12 9.6c1.7.5 2.5 1.9 2.5 4.4" fill="none" stroke="{c}" stroke-width="1.4"/>',
    "repo": '<path d="M3 1.5h9.5v13H5a2 2 0 0 1-2-2z" fill="none" stroke="{c}" stroke-width="1.4"/><path d="M3 12.5a2 2 0 0 1 2-2h7.5" fill="none" stroke="{c}" stroke-width="1.4"/>',
}


def fade_in(i, offset=0.0):
    """Aparece con un pequeño retraso escalonado; si el navegador no anima, se ve el estado final."""
    delay = offset + 0.08 * i
    dur = delay + 0.5
    return (f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{delay/dur:.3f};1" '
            f'dur="{dur:.2f}s" fill="freeze"/>')

def stats_card(theme):
    p = PALETTE[theme]
    rows = [("star", "Total stars", stars), ("commit", "Total commits", commits), ("pr", "Pull requests", prs),
            ("issue", "Issues", issues), ("people", "Followers", user.get("followers", 0)),
            ("repo", "Public repos", user.get("public_repos", 0))]
    w, h = 420, 190
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">',
           f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="{p["bg"]}" stroke="{p["border"]}"/>',
           f'<text x="24" y="34" font-size="17" font-weight="700" fill="{p["title"]}">{escape(user.get("name") or USER)} · GitHub stats</text>']
    y = 62
    col = 0
    for i, (icon, label, value) in enumerate(rows):
        x = 24 + (col * 200)
        out.append(f'<g transform="translate({x},{y-12})">{fade_in(i)}'
                   f'{ICONS[icon].format(c=p["icon"])}'
                   f'<text x="24" y="13" font-size="13.5" fill="{p["text"]}">{label}</text>'
                   f'<text x="168" y="13" font-size="13.5" font-weight="700" fill="{p["text"]}" text-anchor="end">{fmt(value)}</text></g>')
        col += 1
        if col == 2:
            col = 0
            y += 40
    out.append(f'<text x="24" y="{h-14}" font-size="10.5" fill="{p["muted"]}">public activity · updated daily</text>')
    out.append('</svg>')
    return "\n".join(out)


def langs_card(theme):
    p = PALETTE[theme]
    w, h = 420, 190
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">',
           f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" fill="{p["bg"]}" stroke="{p["border"]}"/>',
           f'<text x="24" y="34" font-size="17" font-weight="700" fill="{p["title"]}">Most used languages</text>',
           f'<rect x="24" y="52" width="{w-48}" height="10" rx="5" fill="{p["track"]}"/>']
    x = 24
    for lang, b in langs:
        seg = (w - 48) * b / total_bytes
        color = LANG_COLORS.get(lang, p["accent"])
        out.append(f'<rect x="{x:.1f}" y="52" width="{seg:.1f}" height="10" fill="{color}"><animate attributeName="width" values="0;{seg:.1f}" dur="0.9s" fill="freeze"/></rect>')
        x += seg
    y = 88
    for i, (lang, b) in enumerate(langs):
        cx = 24 + (i % 2) * 200
        cy = y + (i // 2) * 30
        color = LANG_COLORS.get(lang, p["accent"])
        pct = 100 * b / total_bytes
        out.append(f'<g>{fade_in(i, 0.15)}'
                   f'<circle cx="{cx+6}" cy="{cy-4}" r="6" fill="{color}"/>'
                   f'<text x="{cx+20}" y="{cy}" font-size="13.5" fill="{p["text"]}">{escape(lang)}</text>'
                   f'<text x="{cx+168}" y="{cy}" font-size="13.5" font-weight="700" fill="{p["text"]}" text-anchor="end">{pct:.1f}%</text></g>')
    if not langs:
        out.append(f'<text x="24" y="100" font-size="13" fill="{p["muted"]}">No public code yet</text>')
    out.append('</svg>')
    return "\n".join(out)


os.makedirs(OUT, exist_ok=True)
for theme in ("light", "dark"):
    open(f"{OUT}/stats-{theme}.svg", "w", encoding="utf-8").write(stats_card(theme))
    open(f"{OUT}/langs-{theme}.svg", "w", encoding="utf-8").write(langs_card(theme))
print("stars", stars, "commits", commits, "prs", prs, "issues", issues, "langs", langs)
