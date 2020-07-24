FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /project

RUN pip install pipenv -i https://pypi.douban.com/simple

COPY Pipfile /project/Pipfile
COPY Pipfile.lock /project/Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./compose/production/nginx /project

COPY ./compose/production/django/start.sh /start.sh
#RUN sed -i 's\\n\\' /start.sh
RUN chmod +x /start.sh
