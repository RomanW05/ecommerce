FROM python:3

COPY .requirements.txt /backend_user/requirements.txt

WORKDIR /backend_user

RUN pip3 install -r requirements.txt

COPY . /api

CMD ["python", "kafka_consumer.py" ]