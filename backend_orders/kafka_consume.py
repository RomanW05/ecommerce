import json
from kafka import KafkaConsumer, KafkaProducer
import pickle

def cons(request):
    consumer = KafkaConsumer('Ptopic', 
        bootstrap_servers=['localhost:9092'], 
        api_version=(0, 10) 
        #,consumer_timeout_ms=1000
    )

    for message in consumer:
        deserialized_data = pickle.loads(message.value) 
        print(deserialized_data)