#!/usr/bin/env bash

cd ..
docker-compose -f docker-compose-for-django-dev.yml run django python /code/manage.py makemigrations --noinput
# TODO find how to remove container after job done.
#docker-compose -f docker-compose-for-django-dev.yml stop django && docker-compose rm -f docker-compose-for-django-dev.yml django