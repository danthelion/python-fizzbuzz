#!/usr/bin/env bash

python3 -m pytest --junitxml results.xml fizzbuzz-test.py
pep8 --max-line-length=120 fizzbuzz.py > pep8.log || true