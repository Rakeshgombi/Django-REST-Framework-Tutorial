from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializers
from django.http import JsonResponse

# Create your views here.


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({"invalid_data": "not goot data"}, status=400)
