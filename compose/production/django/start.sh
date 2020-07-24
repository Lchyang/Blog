python manage.py migrate
python manage.py collectstatic --noinput
gunicorn Blog.wsgi:application -w 4 -k gthread -b 0.0.0.0:8002 --chdir=/project
