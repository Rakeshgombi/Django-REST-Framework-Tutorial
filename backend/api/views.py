import json
from django.http import JsonResponse


# Create your views here.
def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET)  # URL query parameters
    # print(request.POST)   # URL query parameters
    body = request.body  # Byte string of JSON Data
    data = {}
    try:
        # Converting the JSON data into a Python dictionary.
        data = json.loads(body)
    except:
        pass
    # print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)   # request.META
    # print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
