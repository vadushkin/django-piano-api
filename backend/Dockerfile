# pull official base image
FROM python:3.10.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

# create a directory for staticfiles
RUN mkdir -p /home/app/staticfiles

# copy requirements.txt
COPY requirements.txt /usr/src/app/

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
