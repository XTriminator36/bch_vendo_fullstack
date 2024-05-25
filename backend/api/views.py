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
            print("Watchtower status is not up. Current status:", status)
            return True
    except (requests.RequestException, ValueError) as e:
        print("Failed to retrieve data from the API:", e)
        return True


# # AJAX GET Reaquest API 
def check_tx_hash(request):
    offline = check_watchtower_status()
    try:
        tx_hash = BchValue.objects.last().tx_hash
        cash_address = CashAddress.objects.last().cash_address
    except AttributeError:
        print("No data found in the database.")
        tx_hash = ""
        cash_address = ""

    data = {
        "hash": tx_hash,
        "offline": offline,
        "bchAddress": cash_address,
    }

    return JsonResponse(data)


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
class create_transaction(APIView):
    def post(self, request):
        #gets the existing product item and its necessary details
        product_item_id = request.data.get('id')

        if not product_item_id:
            return Response({'error': 'Product item ID is required.'}, status=status.HTTP_400_BAD_REQUEST) #will return a response if Product ID is mismatched or no request input
        
        try:
            product_item = ProductItem.objects.all(id=product_item_id) #the requested product ID should equal to the existing product ID in the database
        except ProductItem.DoesNotExist:
            return Response({'error' : 'No Existing Product ID'}, status=status.HTTP_404_NOT_FOUND)

        #Creating the transaction
        product_transaction = ProductTransactions(product_item=product_item)
        product_transaction.save() #saves new product transaction
        
        serializer = ProductTransactionSerializer(product_transaction) #serialized the response
        return Response(serializer.data, status=status.HTTP_201_CREATED) #then returns a response


# Update channel via product code in database
@api_view(['POST'])
def update_channel(request):
    channel = request.data.get('product_code')
    print("Channel: ", channel)
    c = ProductItem.objects.all().last()
    c.product_code = channel

    c.save()

    data = {
        "success": True
    }

    return JsonResponse(data) 

#updates the product quantity upon finish bch transaction
@api_view(['POST'])
def update_quantity(request):

    consume_quantity = request.data.get('num') #requests the data from the fixed quantity being consumed

    #other input requests being serialized
    if "product_code" in request.data:
        product_code = ProductCodeSerializer(data=request.data)
    if "txHash" in request.data:
        tx_hash = TxHashSerializer(data=request.data)

    dispense_check = BchValue.objects.filter(tx_hash=tx_hash, dispensed=True) #set the dispense on being true
    if dispense_check.count() == 0:
        print("Trigerring to dispense...")
        print("Product Code: ", product_code)
    
    BchValue.objects.filter(tx_hash=tx_hash).update(dispensed=True)

    if product_code:
        print('Updating quantity...')
        print('Product Code:', product_code)

        try:
            product = ProductItem.objects.get(product_code=product_code)

            if product.quantity > 0:
                product.quantity -= consume_quantity
                product.save()
                time.sleep(0.5)
                return Response({
                    'message': f'Quantity of product {product_code} reduced by {consume_quantity}'
                    }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Product quantity is already zero, therefore cannot dispense'
                }, status=status.HTTP_400_BAD_REQUEST)
        except ProductItem.DoesNotExist:
            return Response({'error': f'Product with code {product_code} does not exist, try again!'}, status=status.HTTP_404_NOT_FOUND)   
    else:
        return JsonResponse({'success': False})
    
# ----- BCH Products side END ----- #


#Retrieving single data from products
# @api_view(['GET'])
# def viewProductItem(request):
#     get_product_item = ProductItem.objects.all(id)
    

#Retrieving single data from vendos (Can be used for searching)
#Updating a single data from products
#Updating a single data from vendos
#The Deletes
   

    
