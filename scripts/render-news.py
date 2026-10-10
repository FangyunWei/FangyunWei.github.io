"""Render the owner's publication list as static, crawlable HTML."""
import json
import re
from html import escape
from pathlib import Path

root = Path(__file__).resolve().parents[1]
papers = json.loads((root / 'data/publications.json').read_text())
years = sorted({p['year'] for p in papers}, reverse=True)
rows = []
for year in years:
    items = []
    for p in papers:
        if p['year'] != year:
            continue
        title = escape(p['title'])
        if p.get('url'):
            title = f'<a class="paper-title" href="{escape(p["url"], quote=True)}">{title}</a>'
        else:
            title = f'<span class="paper-title">{title}</span>'
        items.append(f'<li>{title}<span class="paper-venue">{escape(p["venue"])}</span></li>')
    rows.append(f'<div class="news-row"><h3>{year}</h3><ul>{"".join(items)}</ul></div>')
news = '<section id="publication" class="section" aria-labelledby="publication-title"><div class="section-label"><h2 id="publication-title">Publication</h2></div><div class="section-body">\n'
news += '\n'.join(rows[:3])
news += '\n<details class="news-archive"><summary>Earlier publications <span>2019–2023</span></summary><div class="archive-content">'
news += '\n'.join(rows[3:])
news += '</div></details>\n</div></section>'
path = root / 'dist/index.html'
html = path.read_text()
html, count = re.subn(r'<section id="publication".*?</section>', lambda _: news, html, flags=re.S)
assert count == 1
path.write_text(html)
print(f'Rendered {len(papers)} owner-provided publication records across {len(years)} years.')
