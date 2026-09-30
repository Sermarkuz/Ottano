# Ottano Gold

Ottano è un'applicazione web autonoma per consultare e confrontare i prezzi dei carburanti. La versione Italia usa gli open data MIMIT; **Ottano Mondo** confronta prezzi e serie per Paese.

Sviluppata da Marco Pugliese · SerMarkuz Lab.

## Avvio rapido

Apri direttamente `ottano.html` nel browser, oppure usa GitHub Pages tramite `index.html`.

Non è richiesta alcuna installazione per l'app già generata.

## File principali

- `ottano.template.html` — sorgente HTML/CSS/JavaScript della versione Italia.
- `build.py` — scarica o legge i CSV MIMIT e rigenera `ottano.html`.
- `ottano.html` — versione Italia pronta all'uso, con dati incorporati.
- `basemap.json` — geometrie di riserva usate quando le mappe esterne non sono disponibili.
- `mondo.template.html` — sorgente di Ottano Mondo.
- `data.json` — dati, cambi e serie storiche usati da Ottano Mondo.
- `build_mondo.py` — rigenera `ottano-mondo.html`.
- `ottano-mondo.html` — versione internazionale pronta all'uso.
- `ottano-logo.svg`, `ottano-logo.png` — marchio e mascotte.
- `manifest.webmanifest` — metadati PWA.
- `NOTICE.md` — fonti, licenze e attribuzioni.

## Aggiornare i dati Italia

Scarica i CSV MIMIT del giorno e rigenera l'app:

```bash
python3 build.py --scarica
```

Oppure usa due CSV già scaricati:

```bash
python3 build.py anagrafica_impianti_attivi.csv prezzo_alle_8.csv
```

Per limitare lo snapshot di riserva a province specifiche:

```bash
python3 build.py --scarica --province BZ,TN
```

## Rigenerare Ottano Mondo

Dopo aver aggiornato `data.json`:

```bash
python3 build_mondo.py
```

## Architettura

La versione Italia mantiene la logica applicativa nel template e incorpora i dati nazionali compressi durante il build. Lo snapshot locale non compresso funge da fallback per browser senza decompressione gzip.

Lo stato utente è conservato nel browser. I servizi esterni comprendono Leaflet, OpenStreetMap, Nominatim, OSRM e le altre fonti elencate in `NOTICE.md`.

## GitHub Pages

`index.html` reindirizza a `ottano.html`. In questo modo il repository può essere pubblicato direttamente dalla root del branch scelto per GitHub Pages.

## Licenza

Codice sotto licenza MIT. Dati, logo e servizi esterni mantengono le rispettive licenze e condizioni indicate in `NOTICE.md`.
