#!/bin/bash

APP_PORT=${PORT:-8000}

# Запуск Gunicorn
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm backend.wsgi:application --bind "0.0.0.0:${APP_PORT}"