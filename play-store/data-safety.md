# Google Play Data Safety — bozza operativa

Questa scheda è preparata in modo prudente sulla base del codice attuale di Ottano Android e della web app caricata nella WebView. Va ricontrollata in Play Console prima dell'invio finale se vengono aggiunti analytics, advertising SDK, login, crash reporting o altri servizi.

## L'app raccoglie o condivide dati utente?
Sì, limitatamente a dati inviati a servizi esterni quando l'utente usa funzioni che li richiedono.

## Posizione
### Posizione precisa
- Raccolta: SÌ, opzionale.
- Condivisione: POTENZIALMENTE SÌ con servizi cartografici/geografici quando necessaria alla funzione richiesta.
- Finalità: funzionalità dell'app.
- Trattamento: su richiesta dell'utente; non usata da SerMarkuz Lab per pubblicità.
- Obbligatoria: NO. L'utente può usare gran parte dell'app senza concedere la posizione.

### Posizione approssimativa
Può essere derivata o trasmessa insieme alla posizione precisa nelle funzioni geografiche. Dichiararla con le stesse finalità se Play Console la richiede separatamente.

## Attività nell'app / interazioni
Le query di ricerca di luoghi e gli estremi di percorso possono essere inviati ai servizi geografici usati dalla web app per eseguire ricerca e routing. Trattamento finalizzato alla funzionalità richiesta. Non vengono usati da Ottano per advertising.

## File e documenti
I CSV/CSV.GZ scelti manualmente tramite selettore Android vengono letti per importare il dataset. Il wrapper Android non richiede accesso generale allo storage e non carica deliberatamente questi file su un server SerMarkuz.

## Dati finanziari
NESSUNO.

## Informazioni personali
NESSUN account, nome, email o numero di telefono richiesto dal codice attuale.

## Messaggi, contatti, foto, video, audio, salute
NESSUNO.

## Identificatori dispositivo
Il codice Android di Ottano non genera un proprio identificatore pubblicitario e non include SDK pubblicitari/analytics. I servizi web esterni possono ricevere dati tecnici standard delle richieste HTTPS, ad esempio indirizzo IP e user agent, secondo le proprie policy.

## Sicurezza
- Traffico applicativo previsto via HTTPS.
- Nessuna vendita di dati personali.
- Nessun account utente.
- I dati di preferenza e diario sono mantenuti localmente nella WebView/local storage salvo modifiche future.

## Servizi esterni da ricontrollare prima dell'invio
- Ministero delle Imprese e del Made in Italy
- OpenStreetMap / tile provider
- Nominatim
- OSRM
- Overpass
- eventuale archivio GitHub usato come fallback dei dati

## Nota importante
Google considera anche i dati trasmessi da una WebView controllata dall'app. Per questo la dichiarazione deve comprendere il comportamento della web app, non soltanto il codice Java del wrapper.
