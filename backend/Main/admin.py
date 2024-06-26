from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'product_quantity', 'product_price')
admin.site.register(ProductItem, ProductAdmin)

#registers BCH transactions to admin site
class BchSellTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'tx_id', 
        'sender_address', 
        'destination_address', 
        'cash_amount', 
        'cash_minus_fee_amount',
        'bch_amount',
        'created_at',
        'transaction_status'
    )
admin.site.register(BchSellTransaction, BchSellTransactionAdmin)

#registers cash address
class CashAddressAdmin(admin.ModelAdmin):
    list_display = ('cash_address', 'created_at')
admin.site.register(CashAddress, CashAddressAdmin)

#registers the product transactions
class ProductTransactionsAdmin(admin.ModelAdmin):
    list_display = ('product_item', 'item_hash', 'tx_hash', 'bch_value', 'is_paid', 'is_cancelled','created_at')
admin.site.register(ProductTransactions, ProductTransactionsAdmin)

admin.site.unregister(Group) #unregisters group

admin.site.site_header = "BCH Vending Machine Admin" #set the name of the admin site header
# admin.site.register(VendoRegistration)






