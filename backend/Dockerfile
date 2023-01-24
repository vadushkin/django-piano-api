FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip3 install poetry
RUN poetry install

COPY . /usr/src/app

RUN poetry run python manage.py migrate

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
