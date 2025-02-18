#!/bin/bash
# sync_translations_to_i18n.sh
# Sincroniza recursivamente el directorio de traducciones del repositorio principal hacia el repositorio i18n.
# Uso: ./sync_translations_to_i18n.sh <release_version>

set -e

if [ $# -lt 1 ]; then
    echo "Uso: $0 <release_version>"
    exit 1
fi

VERSION=$1
LANGUAGES=("en" "es_ES" "ca_ES")

# Directorios (ajusta estas rutas si es necesario)
MAIN_REPO_PATH=$(pwd)  # Repositorio principal
LOCALE_DIR="$MAIN_REPO_PATH/locale"
I18N_REPO_PATH="../Giswater-Documentation-i18n"  # Asumiendo que está en un directorio hermano

echo "Sincronizando archivos de traducción hacia el repositorio i18n para la versión $VERSION..."

for lang in "${LANGUAGES[@]}"; do
    SOURCE_DIR="$LOCALE_DIR/$lang/LC_MESSAGES"
    TARGET_DIR="$I18N_REPO_PATH/$VERSION/locale/$lang/LC_MESSAGES"
    mkdir -p "$TARGET_DIR"
    # Copia recursivamente todo el contenido (archivos y subdirectorios)
    rsync -av --delete "$SOURCE_DIR"/ "$TARGET_DIR"/
    echo "Sincronizado recursivamente $lang a $TARGET_DIR"
done

echo "Sincronización completada para la versión $VERSION."
