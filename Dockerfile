FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get -y install \
    python3-pip python3-dev libpq-dev \
    postgresql postgresql-contrib

RUN python -m pip install --upgrade pip && \
    pip install --upgrade setuptools

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .