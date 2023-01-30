<a name="readme-top"></a>

# Simple PianoAPI

[![Tests Status][run-tests]][run-tests-url]
[![Linters Status][run-linters]][run-linters-url]

### Stack

![](https://img.shields.io/badge/python-3.10.6-blue)
![](https://img.shields.io/badge/django-4.1.5-blue)
![](https://img.shields.io/badge/django--rest--framework-3.14.0-blue)
![](https://img.shields.io/badge/celery-5.2.7-blue)
![](https://img.shields.io/badge/pyjwt-2.6.0-blue)
<br>

![](https://img.shields.io/badge/mypy-0.991-blue)
![](https://img.shields.io/badge/black-22.12.0-blue)
![](https://img.shields.io/badge/flake8-6.0.0-blue)
![](https://img.shields.io/badge/autoflake-2.0.0-blue)

Start
-----

### Clone

```shell
git clone https://github.com/vadushkin/django-piano-api.git
cd backend_piano
```

### Env

Create file `backend/.env` or delete `.example` in the `backend/.env.example` file

Fill in the data in the file `backend/.env`

`.env`

```dotenv
# Default Django Setting
SECRET_KEY=secret_key
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,api,[::1]

# DataBase/Postgres
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Cloudinary
CLOUD_NAME=cloud_name
API_KEY=api_key
API_SECRET=api_secret

# Celery
CELERY_BROKER=redis://redis:6379/0
CELERY_BACKEND=redis://redis:6379/0

```

* [Keys](https://cloudinary.com/) for Cloudinary

### Docker

```docker
docker-compose up -d --build
```

### Ports

* [Nginx](http://localhost:8000/): 8000
* [Flower](http://localhost:5555/): 5555

```docker-compose.yml```

```dockerfile
...

services:
  web:
    ...
    ports:
      - "8000:80"
    ...

  flower:
    ...
    ports:
      - "5555:5555"
    ...
   
  celery:
    ports:
      - "default"
  
  backend:
    ...
    expose:
      - 8000
    ...
    
  redis:
    ports:
      - "default"
    
  db:
    ...
    ports:
      - "5433:5432"
    ...
```

[run-tests]: https://github.com/vadushkin/django-piano-api/actions/workflows/run-tests.yml/badge.svg
[run-tests-url]: https://github.com/vadushkin/django-piano-api/actions
[run-linters]: https://github.com/vadushkin/django-piano-api/actions/workflows/run-linters.yml/badge.svg
[run-linters-url]: https://github.com/vadushkin/django-piano-api/actions


<p align="right"><a href="#readme-top">Up!</a></p>
