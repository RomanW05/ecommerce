def kafka_send_message(producer, topic, data):
    producer.poll(0.0)
    producer.produce(topic, data)
    producer.flush()
    print('message sent')


def extract_request_data(request):
    data = {
        'host': request.headers['Host'],
        'user_agent': request.headers['User-Agent'],
        'accept_language': request.headers['Accept-Language'],
        'cookie': request.headers['Cookie'],
        'request_method': request.META['REQUEST_METHOD'],
    }
    return data