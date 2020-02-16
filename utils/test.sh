#!/bin/bash

set -e
# exit-zero treats all errors as warnings.
flake8 . --exclude=**/*/migrations/* --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
# python tests
pytest -n 4 -c pytest.ini --cov=seeker
# run bandit - A security linter
bandit -r seeker
