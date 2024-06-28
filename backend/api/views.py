from django.utils import timezone
import time
from psycopg2 import IntegrityError
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import *
from Main.models import *
from bitcash.network.meta import Unspent


#retrieving entries of product items
#Method1:
# @api_view(['GET'])
# def getProductItems(request):
#     product_item = ProductItem.objects.all()
#     serializer = ProductItemSerializer(product_item, many = True)
#     return Response(serializer.data)

# DEPRECATED vendo registration
# @api_view(['GET'])
#     #retrieving the registered serial
# def getRegisteredVendo(request):
#     registered_vendo = VendoRegistration.objects.all()
#     serializer = VendoRegSerializer(registered_vendo, many = True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def RegisterVendos(request):
#     serializer = VendoRegSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)


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

@api_view(['POST'])
def addProductItems(request):
    serializer = ProductItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

#APIs still need to create are the ff:

#API about displaying the recieving address on product transactions
class display_walletAddress(generics.ListAPIView):
    queryset = CashAddress.objects.all()
    serializer_class = CashAddressSerializer

# ----- WATCHTOWER side of things START ----- #

WATCHTOWER_API_URL = "https://watchtower.cash/api/status"
WATCHTOWER_TIMEOUT = 5

def check_watchtower_status():
    try:
        response = requests.get(WATCHTOWER_API_URL, timeout=WATCHTOWER_TIMEOUT, verify=False)
        response.raise_for_status()
        data = response.json()
        status = data.get("status")
        if status == "up":
            print("Watchtower status is up! ")
            return False
        else:
            print("Watchtower status is down! Current status:", status)
            return True
    except (requests.RequestException, ValueError) as e:
        print("Failed to retrieve data from the API:", e)
        return True


# AJAX GET Reaquest API 
def check_if_online(request):
    offline = check_watchtower_status()
    data = {
        "offline": offline,
    }

    return JsonResponse(data)
# ----- WATCHTOWER side of things END ----- #


# ----- BCH Products side START ----- #
# Will create an output request out of chosen transaction
class create_product_transaction(APIView):
    def post(self, request, *args, **kwargs):
        #gets the existing product item and its necessary details
        product_code = request.data.get('product_code')
        product_quantity = request.data.get('product_quantity')
        bch_value = request.data.get('bch_value')

        if not product_code:
            return Response({'error': 'Product Code is required.'}, status=status.HTTP_400_BAD_REQUEST) #will return a response if Product ID is mismatched or no request input
        elif not bch_value:
            return Response({'error': 'A certain BCH value is required.'}, status=status.HTTP_400_BAD_REQUEST)
        elif not product_quantity:
            return Response({'error': 'Certain Quantity is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product_item = ProductItem.objects.get(product_code=product_code) #the requested product ID should equal to the existing product ID in the database
        except ProductItem.DoesNotExist:
            return Response({'error' : 'No Existing Product Code'}, status=status.HTTP_404_NOT_FOUND)

        #Creating the transaction
        product_transaction = ProductTransactions(product_item=product_item, product_code=product_code, bch_value=bch_value, product_quantity=product_quantity)
        product_transaction.save() #saves new product transaction
        
        serializer = ProductTransactionSerializer(product_transaction) #serialized the response
        return Response(serializer.data, status=status.HTTP_201_CREATED) #then returns a response

#cancels the recent product transaction
class cancel_product_transaction(APIView):
    def post(self, request, *args, **kwargs):
        cancel_transaction = request.data.get('is_cancelled')

        if cancel_transaction == True:
            cancelled = ProductTransactions.objects.latest('id')
            cancelled.is_cancelled = True
            cancelled.is_paid = False
            cancelled.tx_hash = "---PAYMENT ABORTED---"
            cancelled.recipient = "---NO RECIPIENT---"
            cancelled.bch_value = 0.00000000
            cancelled.total_paid = 0.00000000
            cancelled.paid_timestamp = timezone.now()
            cancelled.save()
            
            return Response(status=status.HTTP_200_OK)
        
        return Response(cancelled.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Checks new/latest product transaction
# class check_new_txhash(APIView):
#     def post(self, request, *args, **kwargs):

#         latest_txhash = ProductTransactions.objects.latest('tx_hash')
#         serializer = TxHashSerializer(latest_txhash)

#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class get_latest_item_hash(APIView):
    def get(self, request, *args, **kwargs):
        try:
            latest_item_hash = ProductTransactions.objects.latest('created_at')

            serializer = ProductItemHashSerializer(latest_item_hash)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ProductTransactions.DoesNotExist:
            return Response({"detail": "No transactions found"}, status=status.HTTP_404_NOT_FOUND)
        
    
class check_if_paid_product_hash(APIView):
    def post(self, request, *args, **kwargs):

        product_item_hash = request.data.get('item_hash')

        get_is_paid = ProductTransactions.objects.filter(item_hash=product_item_hash).get().is_paid

        if get_is_paid == True:
            return Response("Successfully Paid", status=status.HTTP_200_OK)

        else:
            return Response("Not yet paid", status=status.HTTP_200_OK)


#updates the product quantity upon finish bch product transaction
# class update_quantity(APIView):
#     def post(self, request, *args, **kwargs):

#         get_current_txhash = request.data.get('txhash')
#         latest_txhash = ProductTransactions.objects.get(tx_hash=get_current_txhash)
#         latest_product_quantity = latest_txhash.product_quantity

#         get_product_stock = ProductItem.objects.get(product_code=latest_txhash.product_code)
#         get_stock_quantity = get_product_stock.product_quantity
        
#         #compares txhashes first before updating product quantity
#         if get_current_txhash != ProductTransactions.objects.latest('tx_hash'):

#         #calculate the current quantity and stock quantity
#             calc_product_quantity = get_stock_quantity - latest_product_quantity

#         #sets a new quantity then updates it
#             set_new_quantity = ProductItem.objects.filter(product_code=latest_txhash.product_code).update(product_quantity=calc_product_quantity) 

#             return Response(set_new_quantity, status=status.HTTP_200_OK)
        
#         else:

#             return Response(status=status.HTTP_400_BAD_REQUEST)
   
    
# ----- BCH Products side END ----- #


#Retrieving single data from products
# @api_view(['GET'])
# def viewProductItem(request):
#     get_product_item = ProductItem.objects.all(id)
    

#Retrieving single data from vendos (Can be used for searching)
#Updating a single data from products
#Updating a single data from vendos
#The Deletes
   

    
