FROM python:3

COPY /ecommerce/backend_analytics/requirements.txt /backend_analytics/requirements.txt

WORKDIR /backend_analytics

RUN pip3 install -r requirements.txt

COPY /ecommerce/backend_analytics /backend_analytics

COPY .env /backend_analytics/

ARG POSTGRES_USER=$POSTGRES_USER
ARG POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ARG POSTGRES_DB=$POSTGRES_DB
ARG POSTGRES_HOST=$POSTGRES_HOST

ENV POSTGRES_HOST=$POSTGRES_HOST

RUN python create_db.py

CMD ["python", "-u", "kafka_consume.py" ]