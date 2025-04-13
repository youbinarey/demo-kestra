#!/bin/bash
# encode_vars.sh

output=".env_encoded"
> "$output"  # Limpiar contenido anterior

while IFS='=' read -r key value; do
  if [[ "$key" != "" && "$value" != "" ]]; then
    encoded=$(echo -n "$value" | base64)
    echo "SECRET_$key=$encoded" >> "$output"
  fi
done < .env

echo "✅ Archivo .env_encoded generado."
