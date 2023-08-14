FROM python:3

COPY /backend_orders/requirements.txt /backend_orders/requirements.txt

WORKDIR /backend_orders

RUN pip3 install -r requirements.txt

COPY /backend_orders /backend_orders

CMD ["python", "kafka_consume.py" ]