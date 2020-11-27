flask db upgrade;
#gunicorn "blogsley_flask:create_app()"
gunicorn -b 0.0.0.0:8000 -k gevent "blogsley_flask:create_app()"