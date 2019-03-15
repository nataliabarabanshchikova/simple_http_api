# HTTP API README #

This repository contains simple web application that written with `django` and `django-rest-framework`. The web service provides REST API for manipulate note objects. REST API includes next methods:
```
POST /notes/
GET /notes/
GET /notes/<note_id>/
PUT /notes/<note_id>/
```

Version 0.1.0

### Setup ###

* Make sure `docker` is installed on system
* Run following commands:
```
:::bash
$ git clone https://github.com/nataliabarabanshchikova/simple_http_api.git
$ cd simple_http_api
$ docker build -t nataliabarabanshchikova/http_api .
$ docker run -d -p 8080:8000 nataliabarabanshchikova/http_api
```
* Open ` http://localhost:8080/notes/` in your browser to check that web service run successful