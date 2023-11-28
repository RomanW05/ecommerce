from inventory_mapping import create_session

from confluent_kafka import Consumer

import os
import sys

session = create_session()

host = os.environ.get('KAFKA_BROKERCONNECT')


consumer = Consumer({
    'bootstrap.servers': host,
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['mytopic'])

print('subscribed\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

while True:
    print('requesting msg')
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

consumer.close()