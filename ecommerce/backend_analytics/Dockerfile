FROM python:3

COPY /ecommerce/backend_analytics/requirements.txt /backend_analytics/requirements.txt

WORKDIR /backend_analytics

RUN pip3 install -r requirements.txt

COPY /ecommerce/backend_analytics /backend_analytics

COPY .env /backend_analytics/

RUN python create_db.py

CMD ["python", "-u", "kafka_consume.py" ]