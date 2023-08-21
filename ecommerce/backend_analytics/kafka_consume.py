from confluent_kafka import Consumer
import json
import time
import psycopg2
import os


conf = {'bootstrap.servers': "kafka1:19091",
        'group.id': "my-group",
        'auto.offset.reset': 'smallest'}
consumer = Consumer(conf)
consumer.subscribe(['analytics'])
print('kafka consume active')
x = 0
while True:
    if x == 15:
        print('pending')
        x = 0
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

    connection = psycopg2.connect(user=os.environ['POSTGRES_USER'],
                                password=os.environ['POSTGRES_PASSWORD'],
                                host=os.environ['POSTGRES_HOST'],
                                port=os.environ['POSTGRES_PORT'],
                                database=os.environ['POSTGRES_DB'])
    print('accepted')
    connection.close()
    time.sleep(1)
    
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
    import psycopg2
    try:
        conn = psycopg2.connect("host=0.0.0.0 dbname=analytics_database")
        conn.close()
    except psycopg2.OperationalError as ex:
        print("Connection failed: {0}".format(ex))
    time.sleep(1)