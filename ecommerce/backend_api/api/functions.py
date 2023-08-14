def create_request_meta_json_object(meta_data):
    return {
        'GATEWAY_INTERFACE': meta_data['GATEWAY_INTERFACE'],
        'SERVER_PORT': meta_data['SERVER_PORT'],
        'REMOTE_HOST': meta_data['REMOTE_HOST'],
        'CONTENT_LENGTH': meta_data['CONTENT_LENGTH'],
        'SCRIPT_NAME': meta_data['SCRIPT_NAME'],
        'SERVER_PROTOCOL': meta_data['SERVER_PROTOCOL'],
        'SERVER_SOFTWARE': meta_data['SERVER_SOFTWARE'],
        'REQUEST_METHOD': meta_data['REQUEST_METHOD'],
        'PATH_INFO': meta_data['PATH_INFO'],
        'QUERY_STRING': meta_data['QUERY_STRING'],
        'REMOTE_ADDR': meta_data['REMOTE_ADDR'],
        'CONTENT_TYPE': meta_data['CONTENT_TYPE'],
        'HTTP_HOST': meta_data['HTTP_HOST'],
        'HTTP_USER_AGENT': meta_data['HTTP_USER_AGENT'],
        'HTTP_ACCEPT': meta_data['HTTP_ACCEPT'],
        'HTTP_ACCEPT_LANGUAGE': meta_data['HTTP_ACCEPT_LANGUAGE'],
        'HTTP_ACCEPT_ENCODING': meta_data['HTTP_ACCEPT_ENCODING'],
        'HTTP_DNT': meta_data['HTTP_DNT'],
        'HTTP_CONNECTION': meta_data['HTTP_CONNECTION'],
        'HTTP_COOKIE': meta_data['HTTP_COOKIE'],
        'HTTP_UPGRADE_INSECURE_REQUESTS': meta_data['HTTP_UPGRADE_INSECURE_REQUESTS'],
        'HTTP_SEC_FETCH_DEST': meta_data['HTTP_SEC_FETCH_DEST'],
        'HTTP_SEC_FETCH_MODE': meta_data['HTTP_SEC_FETCH_MODE'],
        'HTTP_SEC_FETCH_SITE': meta_data['HTTP_SEC_FETCH_SITE'],
        'HTTP_SEC_FETCH_USER': meta_data['HTTP_SEC_FETCH_USER'],
    }


def kafka_send_message(producer, topic, data):
    producer.poll(0.0)
    producer.produce(topic, data)
    producer.flush()
    print('message sent')