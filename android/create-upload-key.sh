#!/usr/bin/env bash
set -euo pipefail

OUT="${1:-ottano-upload.jks}"
ALIAS="${2:-ottano-upload}"

echo "Creo la upload key di Ottano in: $OUT"
echo "Conserva questo file in luogo sicuro. NON committarlo nel repository."

keytool -genkeypair -v \
  -keystore "$OUT" \
  -alias "$ALIAS" \
  -keyalg RSA \
  -keysize 4096 \
  -validity 10000

echo
echo "Ora codifica il keystore per GitHub Actions:"
echo "base64 -w 0 '$OUT' > ottano-upload.base64"
echo
echo "Aggiungi il contenuto come secret OTTANO_KEYSTORE_BASE64 e configura anche:"
echo "OTTANO_KEYSTORE_PASSWORD"
echo "OTTANO_KEY_ALIAS=$ALIAS"
echo "OTTANO_KEY_PASSWORD"
