gunicorn --bind=0.0.0.0 --timeout 600 my_django_app_collection.wsgi

python -m celery -A my_django_app_collection worker -l INFO

python -m celery -A my_django_app_collection  beat  -l info

