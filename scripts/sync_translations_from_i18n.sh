#!/bin/bash
# sync_translations_from_i18n.sh
# Sincroniza las traducciones aprobadas desde el repositorio i18n hacia el repositorio principal.
# No elimina archivos locales ya existentes.
# Uso: ./sync_translations_from_i18n.sh <release_version>

set -e

if [ $# -lt 1 ]; then
    echo "Uso: $0 <release_version>"
    exit 1
fi

VERSION=$1
LANGUAGES=("en" "es_ES" "ca_ES")

# Directorios (ajusta estas rutas si es necesario)
MAIN_REPO_PATH=$(pwd)  # Directorio del repositorio principal
LOCALE_DIR="$MAIN_REPO_PATH/locale"
I18N_REPO_PATH="../Giswater-Documentation-i18n"  # Ubicación del repo i18n

echo "Sincronizando traducciones desde el repositorio i18n para la versión $VERSION..."

for lang in "${LANGUAGES[@]}"; do
    SOURCE_DIR="$I18N_REPO_PATH/$VERSION/locale/$lang/LC_MESSAGES"
    TARGET_DIR="$LOCALE_DIR/$lang/LC_MESSAGES"
    mkdir -p "$TARGET_DIR"
    rsync -av "$SOURCE_DIR"/ "$TARGET_DIR"/
    echo "Copiados archivos de $lang a $TARGET_DIR"
done

echo "Sincronización completada para la versión $VERSION."
