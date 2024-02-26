#!/bin/sh

set -e
poetry run python manage.py wait_for_db
poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate

poetry run python manage.py loaddata src/apps/agriculture/fixtures/PlantedCropsModel.json
poetry run python manage.py loaddata src/apps/region/fixtures/CountryModel.json
poetry run python manage.py loaddata src/apps/region/fixtures/StateModel.json
poetry run python manage.py loaddata src/apps/region/fixtures/CityModel.json


poetry run uwsgi --socket :9000 --workers 4 --master --enable-threads --module config.wsgi
