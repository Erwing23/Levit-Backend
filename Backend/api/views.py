import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body  # byte string of json
    data = {}
    print(request.GET)
    try:
        data = json.loads(body)  # json -> python Dict
    except:
        pass

    print(data)
    #data['headers'] = request.headers
    data['content-type'] = dict(request.content_type)
    data["params"] = dict(request.GET)
    return JsonResponse(data)
