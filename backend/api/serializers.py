from rest_framework import serializers
from Main.models import *

class ProductItemSerializer(serializers.ModelSerializer):
    class Meta: #serializing the data of every input fields
        model = ProductItem
        fields = ('__all__')

class VendoRegSerializer(serializers.ModelSerializer):
    class Meta: #serializing the registered vendos
        model = VendoRegistration
        fields = ('__all__')