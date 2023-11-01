#!/bin/sh
coverage run -m unittest
coverage report -m
exit ${PIPESTATUS[0]}
