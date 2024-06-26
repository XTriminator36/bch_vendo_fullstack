from django.urls import path
from . import views

urlpatterns = [
    #add paths for api functions
    # path('RegisteredVendos/',views.getRegisteredVendo), #DEPRECATED VENDO REGISTRATION
    # path('registerVendos/', views.RegisterVendos), #DEPRECATED VENDO REGISTRATION
    
    # path('ProductItems/', views.getProductItems), #Method1
    path('ProductItems/', views.getProductItems.as_view()), #Method2
    path('ProductItem/<int:pk>', views.getProductItem.as_view()), #get specific product item
    path('addProductItems/', views.addProductItems), # get all product items
    path('wallet-address/', views.display_walletAddress.as_view()), # get bch wallet address
    path('create_product_transaction/', views.create_product_transaction.as_view()), # creates transaction || STILL ON THE WORKS
    path('cancel_product_transaction/', views.cancel_product_transaction.as_view()), # cancels the product transaction
    path('get_latest_item_hash/', views.get_latest_item_hash.as_view()), #gets the latest product item hash
    path('check_if_paid_product_hash/', views.check_if_paid_product_hash.as_view()), #checks if the pending item hash is paid
    #path('',''),
]

#Note:
# add '.as_view()' if view has generic API class~