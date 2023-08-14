from confluent_kafka import Consumer
import pickle


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
        print("Consumer error: ", pickle.loads(msg.value()))
        continue

    message = pickle.loads(msg.value())
    print('message received:', message)
    print(type(message))  # type dictionary