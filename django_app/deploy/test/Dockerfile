FROM python:3.8.0-alpine

RUN mkdir /app
WORKDIR /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

ENTRYPOINT ["./deploy/test/entrypoint.sh"]
