FROM python:3.10.13-slim

RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc

WORKDIR /app

COPY /microservice_users/requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY /microservice_users /app/

COPY wait-for-it.sh /wait-for-it.sh

RUN chmod +x /wait-for-it.sh

ENV DATABASE_NAME POSTGRES_DB
ENV USER POSTGRES_USER
ENV PASSWORD POSTGRES_PASSWORD
ENV HOST POSTGRES_HOST
ENV PORT POSTGRES_PORT
ENV DJANGO_SECRET_KEY DJANGO_SECRET_KEY

COPY ./microservice_inventory/entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]