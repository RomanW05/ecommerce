import httpagentparser

def kafka_send_message(producer, topic, data):
    producer.poll(0.0)
    producer.produce(topic, data)
    producer.flush()
    print('message sent')


def extract_request_data(request):
    os = system_detection(request)
    ip = get_client_ip(request)
    action = url_method(request)
    data = {
        'host': request.headers['Host'],
        'user_agent': request.headers['User-Agent'],
        'accept_language': request.headers['Accept-Language'],
        'cookie': request.headers['Cookie'],
        'request_method': request.META['REQUEST_METHOD'],
        'ip': ip,
        'os': os,
        'action': action,
    }
    return data

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def system_detection(request):
    user_agent = request.headers['User-Agent']
    os_dict = httpagentparser.detect(user_agent)["os"]
    os_str = f'{os_dict["name"]} {os_dict["version"]}'
    return os_str


def url_method(request):
    method = request.META['REQUEST_METHOD']
    url = request.META['PATH_INFO']
    resolution = url + method
    return resolution