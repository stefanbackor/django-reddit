#!/bin/bash

cd /serve/app

python manage.py migrate          # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

python manage.py graphql_schema   # generate graphql schema for Relay graphql client

set -e
exec "$@"
