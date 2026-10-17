# Ottano Gold 4.0

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

## Novità 4.0 — precisione dei dati e delle simulazioni

- Catalogo auto separato dai nove carburanti: ripristinati i modelli Seat, Skoda e gli altri finiti erroneamente nella barra carburanti.
- Per ogni prodotto e servizio viene prima selezionata la comunicazione più recente, mantenendo i secondi. A parità di timestamp e dati discordanti si conserva il prezzo maggiore, per non promettere risparmi non verificati. Solo dopo si confrontano i prodotti della stessa categoria.
- Numeri con virgola decimale e BOM supportati; date impossibili, prezzi non finiti, servizi non riconosciuti e carburanti sconosciuti esclusi. Mediana nazionale corretta anche con numero pari di impianti. Storico e prezzi attuali usano la stessa selezione.
- Calibrazione del consumo con media ponderata sulle distanze, solo per misure pieno-pieno esplicitamente confermate e per la stessa auto/carburante. Le vecchie registrazioni sono conservate, ma non calibrano il modello perché non identificano auto e metodo di misura. Per auto diverse dello stesso modello occorre mantenere un diario distinto.
- Il catalogo contiene consumi indicativi, non dati certificati per anno e allestimento. Per una stima personale usare il proprio consumo misurato. Distanze dalla mappa e costi di deviazione restano stime geometriche, non distanze stradali certificate.
- Questa versione corregge errori deterministici; non dichiara una percentuale di aumento dell'accuratezza su strada. Il prezzo effettivo resta quello esposto alla pompa.

Verifica: `node --test tests/core.test.cjs` (template e app generata). I controlli vengono eseguiti anche in GitHub Actions.
