web: gunicorn world_of_movies.wsgi:application --env DJANGO_SETTINGS_MODULE=world_of_movies.settings --log-file - --access-logfile - --workers 2 --bind 0.0.0.0:$PORT
