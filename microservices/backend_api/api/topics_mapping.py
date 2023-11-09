def assing_topic(request):
    method = request.META['REQUEST_METHOD']
    url = request.META['PATH_INFO']
    resolution = url + method
    match resolution:
        case '/api/home/GET':
            return 'analytics'
        case '/api/home/POST':
            return 'analytics'
        case '/api/home/PUT':
            return 'analytics'
        case '/api/home/DELETE':
            return 'analytics'
    
    return 'analytics'
