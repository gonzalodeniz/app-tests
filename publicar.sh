#!/bin/bash
# Script para publicar en github.
# El codigo local debe estar commited.

# Comprueba que se ha pasado un argumento que corresponde al tag
if [ $# -ne 1 ]; then
    echo "Uso: $0 <tag>"
    exit 1
fi

# Comprueba que no haya cambios pendientes
if [ -n "$(git status --porcelain)" ]; then
    echo "Hay cambios pendientes. Por favor, commitea los cambios antes de publicar."
    exit 1
fi

# Comprueba que el tag no exista
if git rev-parse $1 >/dev/null 2>&1; then
    echo "El tag $1 ya existe. Por favor, elige otro."
    exit 1
fi

# Hace merge en la rama master
git checkout master
git pull --rebase --autostash
git merge develop --no-edit
git push origin master

# Crea el tag y lo publica
git tag -a $1 -m "Publicacion de la version $1"
git push origin $1
