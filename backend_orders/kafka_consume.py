# import json
# from kafka import KafkaConsumer, KafkaProducer
# import pickle

# def cons(topic):
#     consumer = KafkaConsumer(topic, 
#         bootstrap_servers=['localhost:9092'], 
#         api_version=(0, 10) 
#         #,consumer_timeout_ms=1000
#     )

#     for message in consumer:
#         deserialized_data = pickle.loads(message.value) 
#         print(deserialized_data)

# cons('analytics')


# from confluent_kafka import Consumer

# conf = {'bootstrap.servers': "host1:9092,host2:9092",
        # 'group.id': "foo",
        # 'auto.offset.reset': 'smallest'}

# consumer = Consumer(conf)

















from confluent_kafka import Consumer

conf = {'bootstrap.servers': "localhost:9091",
        'group.id': "analytics",
        'auto.offset.reset': 'smallest'}

# while True:
consumer = Consumer(conf)