FROM python:3.7
MAINTAINER Nathan Workman <nathancworkman@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y curl && apt-get -y install sudo
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install -y nodejs yarn
RUN sudo npm install -g gulp

COPY ./package.json /code/package.json
ADD requirements.in /code/

RUN pip install pip==18.1.0
RUN pip install -r requirements.in
RUN yarn

ADD . /code/