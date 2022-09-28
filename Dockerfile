FROM python:3

RUN pip install poetry

ADD . /bot/
WORKDIR /bot
RUN poetry install

