from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import *
from Main.models import *


#retrieving entries of product items
#Method1:
# @api_view(['GET'])
# def getProductItems(request):
#     product_item = ProductItem.objects.all()
#     serializer = ProductItemSerializer(product_item, many = True)
#     return Response(serializer.data)

#Method2:
class getProductItems(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

# @api_view(['GET'])
#retrieving entries of product items
class getProductItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    # return Response(serializer.data)

@api_view(['GET'])
    #retrieving the registered serial
def getRegisteredVendo(request):
    registered_vendo = VendoRegistration.objects.all()
    serializer = VendoRegSerializer(registered_vendo, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addProductItems(request):
    serializer = ProductItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    

@api_view(['POST'])
def RegisterVendos(request):
    serializer = VendoRegSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    

#APIs still need to create are the ff:
#Retrieving single data from products
@api_view(['GET'])
def viewProductItem(request):
    get_product_item = ProductItem.objects.all(id)
    


#Retrieving single data from vendos (Can be used for searching)
#Updating a single data from products
#Updating a single data from vendos
#The Deletes
   

#Creates a generic View and Create type API
# class addProductItems(generics.ListCreateAPIView):
#     queryset = ProductItem.objects.all()
#     serializer_class = ProductItemSerializer
    
