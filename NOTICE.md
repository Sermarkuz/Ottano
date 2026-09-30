# Note su dati, licenze e paternità

- **Codice**: MIT, © 2026 Marco Pugliese (vedi LICENSE). Realizzato da Marco Pugliese con l'assistenza di Claude (Anthropic) per la stesura del codice, su specifiche, scelte di prodotto e revisione dell'autore.
- **Logo e mascotte** (`logo/`): © 2026 Marco Pugliese, licenza Creative Commons BY 4.0. L'uso del nome "Ottano" per prodotti o servizi analoghi non è concesso da questa licenza.
- **Dati carburanti Italia**: Ministero delle Imprese e del Made in Italy, Osservatorio prezzi carburanti, licenza IODL 2.0. La fonte va citata anche nei derivati.
- **Dati Europa/mondo** (`mondo/data.json`): Commissione europea (Weekly Oil Bulletin) e enti nazionali indicati per ciascun Paese; cambi BCE.
- **Servizi esterni** usati a runtime: Leaflet (BSD-2), sfondi cartografici OpenStreetMap, OSM France, Esri World Street Map e OpenTopoMap (attribuzione in mappa; server pubblici con proprie condizioni d'uso, non adatti a traffico elevato), Nominatim e OSRM (server pubblici, senza garanzie: per un uso pubblico intensivo servono istanze proprie), archivio storico `LucaDDDD/benzina-data` (terzi), Frankfurter per i cambi, Overpass API per le colonnine (dati OpenStreetMap, ODbL).
- **Sfondo di riserva** (`src/basemap.json`): confini di regioni e province da openpolis/geojson-italy (dati ISTAT, semplificati), usato solo quando i server delle mappe non sono raggiungibili.
- **Consumi dei modelli** (`CARS` nel sorgente): valori WLTP combinati indicativi raccolti dalle schede tecniche dei costruttori, arrotondati; non sono dati ufficiali e vanno verificati sul libretto. **Tariffe di ricarica**: medie luglio 2026 dell'Osservatorio Adiconsum-TariffEV, modificabili dall'utente.
