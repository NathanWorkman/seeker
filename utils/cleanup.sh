#!/bin/bash

find . -name \*pyc  | xargs  rm -fv
find . -name \*pyo | xargs  rm -fv
find . -name \*~  | xargs  rm -fv
find . -name __pycache__  | xargs  rm -rfv
rm -rf coverage .coverage .cache


