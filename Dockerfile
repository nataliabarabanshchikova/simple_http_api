FROM python:3
MAINTAINER Natalia Barabanshchikova <natalia.barabanschikova@gmail.com>

RUN mkdir /http-api
WORKDIR /http-api
COPY . /http-api/

RUN pip install -r requirements.txt
RUN python ./manage.py migrate
CMD python ./manage.py runserver 0.0.0.0:8000