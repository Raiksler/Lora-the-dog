FROM python:3

ENV TZ="Europe/Moscow"
RUN pip install poetry

ADD . /bot/
WORKDIR /bot
RUN poetry install

