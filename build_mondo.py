#!/usr/bin/env python3
"""Ottano Mondo - build: unisce mondo.template.html, data.json e il logo in ottano-mondo.html.
Per aggiornare i prezzi si modifica data.json (un oggetto per Paese; per i Paesi UE 'hb' e 'hd'
sono le serie settimanali di benzina e gasolio, dalla piu' recente alla piu' vecchia, allineate a 'dates')."""
import re, json, urllib.parse, pathlib
qui = pathlib.Path(__file__).resolve().parent
svg = (qui / "ottano-logo.svg").read_text(encoding="utf-8")
svg = re.sub(r"<!--.*?-->", "", svg); svg = re.sub(r">\s+<", "><", svg).strip()
logo = svg.replace('role="img" aria-label="Ottano, la pompa di benzina sorridente"', 'class="logo" aria-hidden="true"')
fav = "data:image/svg+xml," + urllib.parse.quote(svg, safe="/:=,;' ()")
data = json.dumps(json.loads((qui / "data.json").read_text(encoding="utf-8")), ensure_ascii=False, separators=(",", ":"))
html = (qui / "mondo.template.html").read_text(encoding="utf-8")
for k, v in (("/*LOGO*/", logo), ("/*FAVICON*/", fav), ("/*DATA*/", data)):
    assert html.count(k) == 1, k
    html = html.replace(k, v)
out = qui / "ottano-mondo.html"
out.parent.mkdir(exist_ok=True); out.write_text(html, encoding="utf-8")
print("Fatto:", out, "%.0f KB" % (out.stat().st_size / 1000))
