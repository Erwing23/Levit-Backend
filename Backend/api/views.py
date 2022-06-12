import re
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
       # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "Not good Data"}, status=400)
    """ 
    Serialize Models añadiendo atributos a traves de procesos del mismo modelo
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(model_data, fields=["id", "price", "sale_price"])
        #data["sale_price"] += 12
        data = ProductSerializer(instance).data
    """

    """ 
    GET METHOD REQUEST
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
