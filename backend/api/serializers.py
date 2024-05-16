from rest_framework import serializers
from Main.models import *

# class VendoRegSerializer(serializers.ModelSerializer):
#     class Meta: #serializing the registered vendos
#         model = VendoRegistration
#         fields = ('__all__')

class ProductItemSerializer(serializers.ModelSerializer):
    class Meta: #serializing the data of every input fields
        model = ProductItem
        fields = ('__all__')

class ProductCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('product_code') #serializing only the product code to set as a channel

class ProductTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTransactions
        fields = ['product_item', 'tx_hash', 'recipient', 'created_at']
        read_only_fields = ['transaction_hash', 'created_at']

class TxHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = BchValue
        fields = ('tx_hash')

class IfDispensedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BchValue
        fields = ('dispensed')

class CashAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashAddress
        exclude = ['created_at']

