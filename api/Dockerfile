# pull official base image
FROM python:3.8.1-alpine

RUN apk update && apk add --no-cache  \
    bash \
    git \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/prod.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app/

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "gero.api.wsgi"]
