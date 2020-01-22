#!/bin/bash
FROM python:3.6.10-buster
LABEL Nathan Workman <nathancworkman@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade && apt-get install -y sudo
RUN apt-get install -y git apt-utils build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
