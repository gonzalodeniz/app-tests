#!/bin/bash
# Script para publicar en github

# Comprueba que se ha pasado un argumento que corresponde al tag
if [ $# -ne 1 ]; then
    echo "Uso: $0 <tag>"
    exit 1
fi
