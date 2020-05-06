#!/bin/sh

docker-compose -f docker-compose.dev.yml exec web ./manage.py $@
