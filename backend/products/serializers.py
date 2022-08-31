from rest_framework import serializers

from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            'sale_price',
            'discount',
        ]

    def get_discount(self, obj):
        print(obj.id)
        return obj.get_discount()
