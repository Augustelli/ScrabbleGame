#!/bin/sh

# Ejecuta las pruebas
coverage run -m unittest

# Obtiene el código de retorno de la última ejecución
return_code=$?

# Genera el informe de cobertura
coverage report -m

# Si el código de retorno es 0 (éxito), salimos con 0, de lo contrario, salimos con el código de retorno de las pruebas
if [ $return_code -eq 0 ]; then
  exit 0
else
  exit $return_code
fi
