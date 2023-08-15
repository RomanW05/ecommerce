from confluent_kafka import Consumer
import json


conf = {'bootstrap.servers': "kafka1:19091",
        'group.id': "my-group",
        'auto.offset.reset': 'smallest'}
consumer = Consumer(conf)
consumer.subscribe(['analytics'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: ", msg.value())
        continue
    
    try:
        message = json.loads(msg.value())  # type dictionary
        print('message received:', message)
    except Exception as e:
        print('error parsing data with picke.loads', e)