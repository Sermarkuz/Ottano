# Piano test Google Play — Ottano

## Test interno
Obiettivo: verificare installazione e funzioni native prima del test chiuso.

Casi da provare:
1. Avvio pulito dell'app.
2. Caricamento home Ottano.
3. Permesso posizione: accetta.
4. Permesso posizione: nega.
5. Funzione "Vicino a me".
6. Ricerca luogo.
7. Percorso A → B.
8. Selezione marca/modello auto.
9. Simulatore rifornimento.
10. Apertura Centro dati.
11. Aggiornamento remoto dei dati.
12. Selezione simultanea dei due CSV MIMIT.
13. Importazione di CSV.GZ.
14. Link esterni aperti nel browser.
15. Link Privacy.
16. Tasto Indietro Android.
17. Rotazione schermo.
18. Connessione lenta o assente.

## Test chiuso
Se l'account Play Console è personale ed è stato creato dopo il 13 novembre 2023:
- minimo 12 tester;
- tester aderenti senza interruzioni per almeno 14 giorni;
- usare preferibilmente 15-20 tester per avere margine se qualcuno abbandona;
- raccogliere feedback effettivo durante il periodo.

## Scheda feedback suggerita
Chiedere ai tester:
- modello smartphone e versione Android;
- l'app si apre correttamente?
- mappa caricata?
- geolocalizzazione funzionante?
- ricerca luogo funzionante?
- simulazione comprensibile?
- selezione auto completa?
- import CSV riuscito?
- crash o blocchi?
- suggerimenti UX?

## Prima della produzione
- risolvere crash e ANR del Pre-launch report;
- verificare Data Safety;
- verificare privacy URL;
- verificare che screenshot e descrizioni corrispondano all'app reale;
- incrementare versionCode a ogni nuovo AAB.
