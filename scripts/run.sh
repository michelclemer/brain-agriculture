#!/bin/sh

set -e
# poetry shell  # Remova ou comente esta linha
poetry run python src/manage.py wait_for_db
poetry run python src/manage.py collectstatic --noinput
poetry run python src/manage.py migrate

poetry run python src/manage.py loaddata src/apps/agriculture/fixtures/PlantedCropsModel.json
poetry run python src/manage.py loaddata src/apps/region/fixtures/CountryModel.json
poetry run python src/manage.py loaddata src/apps/region/fixtures/StateModel.json
poetry run python src/manage.py loaddata src/apps/region/fixtures/CityModel.json

poetry run uwsgi --socket :8000 --workers 4 --master --enable-threads --module src.config.wsgi
