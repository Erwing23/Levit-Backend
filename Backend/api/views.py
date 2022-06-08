from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "price"])

    """" 
    body = request.body  # byte string of json
    data = {}
    print(request.GET)
    try:
        data = json.loads(body)  # json -> python Dict
    except:
        pass

    print(data)


    #data['headers'] = dict(request.headers)
    #data['content-type'] = dict(request.content_type)
    data["params"] = dict(request.GET)
    """

    return Response(data)
