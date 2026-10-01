# Ottano Android

Wrapper Android nativo per la web app Ottano.

## Requisiti

- JDK 17
- Android SDK 36
- Android Build Tools 36.0.0
- Gradle 9.6.0
- Android Gradle Plugin 9.4.0

Il progetto usa `applicationId`:

`it.sermarkuz.ottano`

Target: Android 16 / API 36.

## Build locale

Apri la cartella `android/` con Android Studio oppure, con Gradle 9.6 disponibile:

```bash
cd android
gradle :app:assembleDebug
gradle :app:bundleRelease
```

Senza configurazione di firma, il bundle release viene generato non firmato.

## Firma per Google Play

Crea una upload key e configura questi valori come GitHub Actions Secrets:

- `OTTANO_KEYSTORE_BASE64`: contenuto del file .jks codificato in Base64
- `OTTANO_KEYSTORE_PASSWORD`
- `OTTANO_KEY_ALIAS`
- `OTTANO_KEY_PASSWORD`

Il workflow `.github/workflows/android.yml` decodifica temporaneamente il keystore durante la build e genera l'AAB firmato.

Non committare mai il file .jks nel repository.

## Funzioni native

- WebView verso https://sermarkuz.github.io/Ottano/
- JavaScript e DOM storage
- geolocalizzazione con permesso Android
- selezione multipla CSV / CSV.GZ tramite Storage Access Framework
- link esterni aperti nel browser
- navigazione indietro interna
- nessun permesso di accesso generale allo storage
