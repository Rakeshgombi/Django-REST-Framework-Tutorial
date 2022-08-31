from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializers


# Create your views here.
@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Product.objects.all().order_by('?').first()
    # print(model_data)
    data = {}
    if instance:
        # data = model_to_dict(instance,
        #                      fields=['id', 'title', 'price',
        #                              'content', 'sale_price']
        #                      )
        data = ProductSerializers(instance).data
    return Response(data)
