# Checklist Google Play — Ottano

## Account e app
- [ ] Account Google Play Console verificato.
- [ ] Crea nuova app: Ottano.
- [ ] Lingua predefinita: Italiano.
- [ ] Tipo: App.
- [ ] Gratuita.
- [ ] Categoria: Auto e veicoli.
- [ ] Package name: it.sermarkuz.ottano.

## Firma
- [ ] Crea upload key .jks.
- [ ] Abilita Play App Signing.
- [ ] Aggiungi in GitHub Actions Secrets:
  - OTTANO_KEYSTORE_BASE64
  - OTTANO_KEYSTORE_PASSWORD
  - OTTANO_KEY_ALIAS
  - OTTANO_KEY_PASSWORD
- [ ] Esegui workflow Build Android AAB.
- [ ] Scarica artifact app-release.aab.

## Store listing
- [x] Nome: Ottano.
- [x] Testo breve IT.
- [x] Descrizione IT.
- [x] Testo breve EN.
- [x] Descrizione EN.
- [x] URL privacy.
- [ ] Carica icona 512×512.
- [ ] Carica feature graphic 1024×500.
- [ ] Carica almeno 2 screenshot telefono.
- [ ] Eventuale video YouTube, non necessario.

## App content
- [ ] Compila Data Safety usando play-store/data-safety.md come base.
- [ ] Dichiara uso posizione opzionale per funzionalità.
- [ ] Ricontrolla servizi esterni della WebView.
- [ ] Sezione Ads: No, se non vengono aggiunti sistemi pubblicitari.
- [ ] Accesso app: nessun login richiesto.
- [ ] Target audience: adulti / pubblico generale, non specificamente bambini.
- [ ] Content rating questionnaire.
- [ ] App category e contatti sviluppatore.

## Test
- [ ] Internal testing.
- [ ] Test file picker con due CSV.
- [ ] Test permesso posizione: concesso, negato, revocato.
- [ ] Test tasto Indietro.
- [ ] Test offline/errore rete.
- [ ] Test Android 16.
- [ ] Test almeno un dispositivo Android 10/11 (minSdk 26 supporta Android 8.0+).
- [ ] Controlla che privacy.html sia raggiungibile sia dal Play Store sia dall'app.

## Release
- [ ] Upload AAB nel track di test interno.
- [ ] Risolvi eventuali warning Pre-launch report.
- [ ] Promuovi a produzione.
- [ ] Inserisci note versione 1.0.0.
