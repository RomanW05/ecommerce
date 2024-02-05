#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input


if [ "$DJANGO_ENV" = "development" ]; then
    echo "Starting Django development server"
    python manage.py runserver 0.0.0.0:8003
else
    echo "Starting Gunicorn server"
    gunicorn microservice_inventory.wsgi:application --bind 0.0.0.0:8003
fi
