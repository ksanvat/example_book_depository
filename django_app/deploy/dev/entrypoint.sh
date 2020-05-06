#!/bin/sh

if [ "$DB_ENGINE" = "django.db.backends.postgresql" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$DB_AUTO_MIGRATE" = "1" ]
then
    ./manage.py migrate
fi

if [ "$DB_LOADDATA_SAMPLE" = "1" ]
then
    ./manage.py loaddata sample.json
fi


exec "$@"
