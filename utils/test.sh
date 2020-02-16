#!/bin/bash

# stop the build if there are Python syntax errors or undefined names
# flake8 . --exclude=**/*/migrations/*,node_modules --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide

# set -e
# exit-zero treats all errors as warnings.
flake8 . --exclude=**/*/migrations/*,node_modules --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# # python tests
pytest -n 4 -c pytest.ini --cov=seeker

# # run bandit - A security linter from OpenStack Security
bandit -r seeker
