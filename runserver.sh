#!/usr/bin/env bash

source set_env_var.sh

python manage.py makemigrations
python manage.py migrate
python manage.py runserver