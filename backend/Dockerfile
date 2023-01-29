# pull official base image
FROM python:3.10.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create a directory for staticfiles
RUN mkdir -p /home/app/staticfiles

# copy poetry.lock and pyproject.toml
COPY poetry.lock pyproject.toml /usr/src/app/

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry install

# copy project
COPY . /usr/src/app
