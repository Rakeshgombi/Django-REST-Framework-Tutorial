from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by('?').first()
    # print(model_data)
    data = {}
    if model_data:
        data = model_to_dict(model_data,
                             fields=['id', 'title', 'price', 'content']
                             )
    return Response(data)
