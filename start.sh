#!/bin/bash

echo "⚙️ Rodando migrações..."
poetry run python manage.py migrate --noinput

echo "⚙️ Iniciando Gunicorn..."
exec poetry run gunicorn tuitin.wsgi:application --bind 0.0.0.0:8000 --workers 3

echo "🚀 Deu tudo certo! Mete marcha! Randandandandan"