release: python waitress/manage.py migrate
web: gunicorn wsgi --pythonpath=waitress --log-file -
