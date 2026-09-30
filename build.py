#!/usr/bin/env python3
"""Ottano - script di build.

Prende il sorgente (src/ottano.template.html) e ci incorpora i dati MIMIT,
producendo un unico file autonomo: dist/ottano.html

Uso:
  python3 build.py --scarica                      # scarica i CSV di oggi dal sito MIMIT
  python3 build.py anagrafica.csv prezzi.csv      # usa due file gia' scaricati
Opzioni:
  --province BZ,TN   province dello snapshot di riserva (non compresso), default BZ,TN

Solo libreria standard di Python 3.
"""
import sys, re, gzip, base64, argparse, urllib.request, pathlib

MIMIT = "https://www.mimit.gov.it/images/exportCSV/"
QUI = pathlib.Path(__file__).resolve().parent


def leggi(testo):
    """Restituisce (data_estrazione, separatore, righe_dati) di un CSV MIMIT."""
    righe = testo.replace("\r", "").split("\n")
    data, h = "", -1
    for i, r in enumerate(righe[:5]):
        m = re.search(r"Estrazione del\s+(\d{4}-\d{2}-\d{2})", r)
        if m:
            data = m.group(1)
        if r.lower().startswith("idimpianto"):
            h = i
            break
    if h < 0:
        sys.exit("File non riconosciuto come CSV MIMIT")
    sep = "|" if "|" in righe[h] else ";"
    return data, sep, [r for r in righe[h + 1:] if r]


def compatta_anagrafica(testo, province=None):
    data, sep, righe = leggi(testo)
    out, ids = [], set()
    for r in righe:
        f = r.split(sep)
        n = len(f)
        if n < 10:
            continue
        try:
            lat, lon = float(f[n - 2]), float(f[n - 1])
        except ValueError:
            continue
        if province and f[n - 3].strip() not in province:
            continue
        # il nome impianto puo' contenere il separatore: si ricompone dal centro
        nome = " ".join(" ".join(f[4:n - 5]).split())
        out.append("|".join([f[0], "", f[2].strip(), f[3].strip(), nome, " ".join(f[n - 5].split()),
                             f[n - 4].strip(), f[n - 3].strip(), "%.5f" % lat, "%.5f" % lon]))
        ids.add(f[0])
    testa = ("Estrazione del %s\nidImpianto|Gestore|Bandiera|Tipo Impianto|Nome Impianto|"
             "Indirizzo|Comune|Provincia|Latitudine|Longitudine\n" % data)
    return testa + "\n".join(out), ids, data


def compatta_prezzi(testo, ids=None):
    data, sep, righe = leggi(testo)
    out = []
    for r in righe:
        f = r.split(sep)
        if len(f) < 5 or (ids is not None and f[0] not in ids):
            continue
        f[4] = f[4][:16]  # via i secondi dalla data di comunicazione
        out.append("|".join(f[:5]))
    return "Estrazione del %s\nidImpianto|descCarburante|prezzo|isSelf|dtComu\n" % data + "\n".join(out)


def gz64(s):
    return base64.b64encode(gzip.compress(s.encode("utf-8"), 9, mtime=0)).decode()


def main():
    ap = argparse.ArgumentParser(description="Build di Ottano")
    ap.add_argument("anagrafica", nargs="?")
    ap.add_argument("prezzi", nargs="?")
    ap.add_argument("--scarica", action="store_true")
    ap.add_argument("--province", default="BZ,TN")
    a = ap.parse_args()

    if a.scarica:
        def get(nome):
            print("Scarico", nome)
            req = urllib.request.Request(MIMIT + nome, headers={"User-Agent": "Mozilla/5.0"})
            return urllib.request.urlopen(req, timeout=120).read().decode("utf-8", "replace")
        ta, tp = get("anagrafica_impianti_attivi.csv"), get("prezzo_alle_8.csv")
    elif a.anagrafica and a.prezzi:
        ta = pathlib.Path(a.anagrafica).read_text(encoding="utf-8", errors="replace")
        tp = pathlib.Path(a.prezzi).read_text(encoding="utf-8", errors="replace")
    else:
        ap.error("indica i due CSV oppure usa --scarica")

    naz_a, _, data = compatta_anagrafica(ta)
    naz_p = compatta_prezzi(tp)
    loc_a, ids, _ = compatta_anagrafica(ta, set(a.province.split(",")))
    loc_p = compatta_prezzi(tp, ids)
    for nome, s in (("anagrafica", loc_a), ("prezzi", loc_p)):
        if "</script" in s.lower():
            sys.exit("Lo snapshot %s contiene '</script': va ripulito prima di incorporarlo" % nome)

    html = (QUI / "src" / "ottano.template.html").read_text(encoding="utf-8")
    basemap = (QUI / "src" / "basemap.json").read_text(encoding="utf-8").strip()
    for segnaposto, valore in (("/*BASEMAP*/", basemap), ("/*NAT_A*/", gz64(naz_a)), ("/*NAT_P*/", gz64(naz_p)),
                               ("/*SNAP_A*/", loc_a), ("/*SNAP_P*/", loc_p)):
        if html.count(segnaposto) != 1:
            sys.exit("Segnaposto %s non trovato nel template" % segnaposto)
        html = html.replace(segnaposto, valore)
    dest = QUI / "dist" / "ottano.html"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("Fatto: %s (%.1f MB), dati del %s, %d impianti"
          % (dest, dest.stat().st_size / 1e6, data, naz_a.count("\n") - 1))


if __name__ == "__main__":
    main()
