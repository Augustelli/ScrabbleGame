#!/bin/bash

VENV_NAME="venv"

if [ -d "$VENV_NAME" ]; then
  echo "El entorno virtual $VENV_NAME ya existe."
else
  python3 -m venv "$VENV_NAME"
  echo "Entorno virtual $VENV_NAME creado con Python 3."
fi

source "$VENV_NAME/bin/activate"
echo "Entorno virtual $VENV_NAME activado."

if ! command -v pip &> /dev/null; then
  echo "pip no está instalado. Instalando pip..."
  python -m ensurepip --default-pip
  echo "pip instalado."
fi

pip install -r requirements.txt
echo "Dependencias instaladas."

deactivate
echo "Entorno virtual $VENV_NAME desactivado."
