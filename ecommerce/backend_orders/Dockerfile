FROM python:3

COPY /ecommerce/backend_orders/requirements.txt /backend_orders/requirements.txt

WORKDIR /backend_orders

RUN pip3 install -r requirements.txt

COPY /ecommerce/backend_orders /backend_orders

CMD ["python", "kafka_consume.py" ]