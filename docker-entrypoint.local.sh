#!/bin/sh
python manage.py collectstatic --no-input
#python manage.py makemigrations --merge --noinput
pip install -r requirements.txt
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000
