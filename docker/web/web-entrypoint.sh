#!/bin/bash

cd seeker
gulp build
python manage.py migrate
python manage.py collectstatic --no-input
gulp
