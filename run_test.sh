#!/bin/sh

coverage run -m unittest && coverage report -m

return_code=$?

if [ $return_code -eq 0 ]; then
  echo "Tests PASSED"
  exit 0
else
  echo "Tests FAILED"
  exit 1
fi
