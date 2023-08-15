from .custom_validators import char_validator, int_validator

def create_request_meta_json_object(meta_data):
    # string_data = [
    #     'GATEWAY_INTERFACE',
    #     'SERVER_PORT',
    #     'REMOTE_HOST',
    #     'CONTENT_LENGTH',
    #     'SCRIPT_NAME',
    #     'SERVER_PROTOCOL',
    #     'SERVER_SOFTWARE',
    #     'REQUEST_METHOD',
    #     'PATH_INFO'
    #     'QUERY_STRING',
    #     'REMOTE_ADDR',
    #     'CONTENT_TYPE',
    #     'HTTP_HOST'
    #     'HTTP_USER_AGENT',
    #     'HTTP_ACCEPT',
    #     'HTTP_ACCEPT_LANGUAGE',
    #     'HTTP_ACCEPT_ENCODING',
    #     'HTTP_DNT',
    #     'HTTP_CONNECTION',
    #     'HTTP_COOKIE',
    #     'HTTP_UPGRADE_INSECURE_REQUESTS',
    #     'HTTP_SEC_FETCH_DEST',
    #     'HTTP_SEC_FETCH_MODE',
    #     'HTTP_SEC_FETCH_SITE',
    #     'HTTP_SEC_FETCH_USER',
    # ]
    # for elem in meta_data.iter():
    #     char_validator(meta_data[elem]) 
    return {
        'GATEWAY_INTERFACE': char_validator(meta_data['GATEWAY_INTERFACE'], 15, 'GATEWAY_INTERFACE'),
        'SERVER_PORT': int_validator(meta_data['SERVER_PORT'], 999999, 'SERVER_PORT'),
        'REMOTE_HOST': char_validator(meta_data['REMOTE_HOST'], 16, 'REMOTE_HOST'),
        'CONTENT_LENGTH': char_validator(meta_data['CONTENT_LENGTH'], 2048, 'CONTENT_LENGTH'),
        'SCRIPT_NAME': char_validator(meta_data['SCRIPT_NAME'], 1024, 'SCRIPT_NAME'),
        'SERVER_PROTOCOL': char_validator(meta_data['SERVER_PROTOCOL'], 256, 'SERVER_PROTOCOL'),
        'SERVER_SOFTWARE': char_validator(meta_data['SERVER_SOFTWARE'], 256, 'SERVER_SOFTWARE'),
        'REQUEST_METHOD': char_validator(meta_data['REQUEST_METHOD'], 128, 'REQUEST_METHOD'),
        'PATH_INFO': char_validator(meta_data['PATH_INFO'], 2048, 'PATH_INFO'),
        'QUERY_STRING': char_validator(meta_data['QUERY_STRING'], 4096, 'QUERY_STRING'),
        'REMOTE_ADDR': char_validator(meta_data['REMOTE_ADDR'], 16, 'REMOTE_ADDR'),
        'CONTENT_TYPE': char_validator(meta_data['CONTENT_TYPE'], 256, 'CONTENT_TYPE'),
        'HTTP_HOST': char_validator(meta_data['HTTP_HOST'], 16, 'HTTP_HOST'),
        'HTTP_USER_AGENT': char_validator(meta_data['HTTP_USER_AGENT'], 256, 'HTTP_USER_AGENT'),
        'HTTP_ACCEPT': char_validator(meta_data['HTTP_ACCEPT'], 128, 'HTTP_ACCEPT'),
        'HTTP_ACCEPT_LANGUAGE': char_validator(meta_data['HTTP_ACCEPT_LANGUAGE'], 16, 'HTTP_ACCEPT_LANGUAGE'),
        'HTTP_ACCEPT_ENCODING': char_validator(meta_data['HTTP_ACCEPT_ENCODING'], 64, 'HTTP_ACCEPT_ENCODING'),
        'HTTP_DNT': char_validator(meta_data['HTTP_DNT'], 16, 'HTTP_DNT'),
        'HTTP_CONNECTION': char_validator(meta_data['HTTP_CONNECTION'], 16, 'HTTP_CONNECTION'),
        'HTTP_COOKIE': char_validator(meta_data['HTTP_COOKIE'], 256, 'HTTP_COOKIE'),
        'HTTP_UPGRADE_INSECURE_REQUESTS': char_validator(meta_data['HTTP_UPGRADE_INSECURE_REQUESTS'], 64, 'HTTP_UPGRADE_INSECURE_REQUESTS'),
        'HTTP_SEC_FETCH_DEST': char_validator(meta_data['HTTP_SEC_FETCH_DEST'], 16, 'HTTP_SEC_FETCH_DEST'),
        'HTTP_SEC_FETCH_MODE': char_validator(meta_data['HTTP_SEC_FETCH_MODE'], 64, 'HTTP_SEC_FETCH_MODE'),
        'HTTP_SEC_FETCH_SITE': char_validator(meta_data['HTTP_SEC_FETCH_SITE'], 1024, 'HTTP_SEC_FETCH_SITE'),
        'HTTP_SEC_FETCH_USER': char_validator(meta_data['HTTP_SEC_FETCH_USER'], 128, 'HTTP_SEC_FETCH_USER'),
    }


def kafka_send_message(producer, topic, data):
    producer.poll(0.0)
    producer.produce(topic, data)
    producer.flush()
    print('message sent')