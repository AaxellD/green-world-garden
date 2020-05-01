release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn greenworld\wsgi.py --log-file -
