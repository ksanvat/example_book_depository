#!/bin/sh

docker-compose -f docker-compose.test.yml exec web ./manage.py $@
