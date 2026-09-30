# Ottano Gold — codice sorgente

App prezzi carburanti in un unico file HTML: mappa di tutta Italia su open data MIMIT, percorso A→B, storico, simulazione del rifornimento, scomposizione del prezzo dal Brent, diario, elettrico (tariffe di ricarica, colonnine da OpenStreetMap) e una tabella di modelli con i consumi WLTP. Con **Ottano Mondo**, prezzi per Paese. Sviluppata da Marco Pugliese · SerMarkuz Lab.

**Provala**: scarica `dist/ottano.html` e aprilo nel browser. Nessuna installazione.

Licenza MIT (vedi `LICENSE`); dati, logo e servizi esterni in `NOTICE.md`. Fork e contributi benvenuti: apri una issue o una pull request.

## Contenuto

- `src/ottano.template.html` — il sorgente vero: HTML, CSS e JavaScript leggibili (circa 90 KB), con quattro segnaposto al posto dei dati (`/*NAT_A*/`, `/*NAT_P*/`, `/*SNAP_A*/`, `/*SNAP_P*/`). È qui che si modifica l'app.
- `build.py` — incorpora i dati MIMIT nel sorgente e produce `dist/ottano.html`. Solo Python 3 standard.
- `dist/ottano.html` — l'app pronta, con i dati del 15/09/2026 (1,9 MB: quasi tutto è l'archivio nazionale compresso).
- `logo/` — la mascotte in SVG e PNG (CC BY 4.0).
- `mondo/` — Ottano Mondo, l'app a parte sui prezzi per Paese: `mondo.template.html` (sorgente), `data.json` (prezzi, cambi, serie UE a 11 settimane, elenco dei Paesi aggiungibili) e `build_mondo.py`, che produce `dist/ottano-mondo.html`. Per aggiornare i prezzi si modifica `data.json` e si rilancia lo script.

## Aggiornare i dati o ricostruire dopo una modifica

    python3 build.py --scarica
    python3 build.py anagrafica_impianti_attivi.csv prezzo_alle_8.csv

Il primo comando scarica i due CSV del giorno dal sito MIMIT, il secondo usa file già scaricati. `--province BZ,TN` sceglie le province dello snapshot di riserva, usato solo dai browser senza decompressione gzip.

Il template funziona anche da solo, senza build: aperto nel browser con la rete attiva scarica i dati all'avvio; senza rete resta vuoto.

## Com'è fatto il sorgente

Due blocchi `<script>`. Il primo, tra `/* ===== CORE` e `/* ===== /CORE`, è la logica pura senza DOM e si può provare con Node (`module.exports` in fondo): lettura dei CSV (`buildDB`), categorie di carburante (`categorize`), filtri e ordinamento (`compute`), statistiche e fasce di colore (`stats`, `band`), distanza dal percorso (`buildRoute`), storico (`parseDay`, `zoneSeries`), quantità della simulazione (`litriFor`). La tabella `CARS` in testa al primo script contiene i modelli con il consumo WLTP combinato: si aggiornano e si ampliano lì. Il secondo è l'interfaccia, per sezioni commentate: dati, interfaccia, mappa, scheda, luogo, percorso, storico, analisi, dal Brent alla pompa, diario, eventi. Nel modulo Brent i valori predefiniti (Brent, cambio, accise temporanee del gasolio in `accisaAuto`) vanno aggiornati a mano nel sorgente quando cambiano.

Lo stato dell'utente sta nell'oggetto `S` (chiave di salvataggio `pieno-v2`), il diario nella chiave `ottano-diario`. Il salvataggio usa `window.storage` nelle anteprime Claude e la memoria del browser altrove.

## Servizi esterni

Leaflet 1.9.4 da cdnjs; carte OpenStreetMap: MapTiler Streets/Outdoor con chiave gratuita dell'utente (sempre funzionanti), poi i server pubblici OSM (tile.openstreetmap.org, OSM Germania, OSM France, OpenTopoMap) ed Esri come riserva, provati in ordine con una tessera di prova (CARTO è stato tolto: dal 2026 richiede una chiave API), con sfondo incorporato di riserva; dati MIMIT (licenza IODL 2.0: va citata la fonte); copia giornaliera e storico dal repository GitHub `LucaDDDD/benzina-data` (di terzi, può sparire); ricerca indirizzi Nominatim (massimo una richiesta al secondo, niente uso massivo); percorsi dal server dimostrativo OSRM (senza garanzie: per un uso pubblico serve un'istanza propria o un servizio a pagamento).
