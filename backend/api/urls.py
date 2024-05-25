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
    path('update_quantity/', views.update_quantity), # updating quantity
    path('wallet-address/', views.display_walletAddress.as_view()), # get bch wallet address
    path('create_transaction', views.create_transaction.as_view()), # creates transaction || STILL ON THE WORKS
    #path('',''),
]

#Note:
# add '.as_view()' if view has generic API class~