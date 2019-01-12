#!/bin/bash

cd seeker
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py runserver
