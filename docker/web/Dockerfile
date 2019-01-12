FROM python:3.6
MAINTAINER Nathan Workman <nathancworkman@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get -y upgrade && apt-get install -y sudo 
ADD requirements.in /code/

RUN pip install pip==9.0.3
RUN pip install -r requirements.in

ADD . /code/
