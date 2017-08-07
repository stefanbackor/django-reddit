FROM python:3.6

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /serve
COPY . /serve/app

WORKDIR /serve
RUN mkdir media static cache logs
VOLUME ["/serve/media/", "/serve/static/", "/serve/cache/", "/serve/logs/"]

WORKDIR /serve/app
RUN pip install -r requirements.txt

EXPOSE 8000
