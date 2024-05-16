from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *

admin.site.register(ProductItem) #registers Product items

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

#register the BCH value into admin site
class BchValueAdmin(admin.ModelAdmin):
    list_display = ('tx_hash', 'bch_value', 'completed', 'created_at', 'dispensed')
admin.site.register(BchValue, BchValueAdmin)

#registers cash address
class CashAddressAdmin(admin.ModelAdmin):
    list_display = ('cash_address', 'created_at')
admin.site.register(CashAddress, CashAddressAdmin)

admin.site.unregister(Group) #unregisters group

admin.site.site_header = "BCH Vending Machine Admin" #set the name of the admin site header
# admin.site.register(VendoRegistration)






