from confluent_kafka import Consumer

conf = {'bootstrap.servers': "kafka1:19091",
        'group.id': "analytics",
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)
consumer.subscribe(['analytics'])


while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))