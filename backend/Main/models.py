from io import BytesIO
import sys
import PIL
from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
import requests
import hashlib
import uuid

# Create your models here.

# ----- DEPRECATED VENDO REGISTRATION -----
# class VendoRegistration(models.Model):
#     PI_CHOICES = [
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#     ]
#     pi_model = models.IntegerField(default=0)
#     serial_number = models.CharField(max_length = 16, default='')
#     bch_wallet_address = models.CharField(max_length = 50, default='')
#     bch_vendo_name = models.CharField(max_length = 50, default='')
#     product_items_available = models.IntegerField(default=0)

#     def __str__(self):
#         return self.bch_vendo_name

#     class Meta:
#         verbose_name_plural = 'Vendo Registration'
# ----- DEPRECATED VENDO REGISTRATION -----

# ----- Alarm records
class Alarm(models.Model):
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.enable

    class Meta:
        verbose_name_plural = 'Alarm'


# ----- Vendo's BCH recieving address for BCH Product Tranactions
class CashAddress(models.Model):
    cash_address = models.CharField(max_length = 54, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.cash_address

    class Meta:
        verbose_name_plural = 'Cash Addresses'

# ----- Products Table
class ProductItem(models.Model):
    # bch_vendo = models.ForeignKey(VendoRegistration, on_delete=models.CASCADE, default=1)

    # product code choices
    PRODUCT_CODES = [
        ('A01', 'A01'),
        ('A02', 'A02'),
        ('A03', 'A03'),
        ('A04', 'A04'),
        ('B05', 'B05'),
        ('B06', 'B06'),
        ('B07', 'B07'),
        ('B08', 'B08'),
        ('C09', 'C09'),
        ('C10', 'C10'),
        ('C11', 'C11'),
        ('C12', 'C12'),
        ('D13', 'D13'),
        ('D14', 'D14'),
        ('D15', 'D15'),
        ('D16', 'D16'),
    ]
    product_code = models.CharField(max_length = 3, choices= PRODUCT_CODES)
    product_name = models.CharField(max_length = 50, default='')
    product_quantity = models.IntegerField(default=0)   
    product_price = models.DecimalField(max_digits = 10, decimal_places=2)
    product_image = models.ImageField(upload_to='products')

    # --- overrides save functionality for the product images 
    def save(self, *args, **kwargs):
        if self.product_image:
            res_img = Image.open(self.product_image) #reinstantiate the product image for rescaling
            max_width = 112
            max_height = 160

            # if res_img.mode == 'RGBA':
            #     res_img = res_img.convert('RGB') #converts from an RGBA format image to RGB

            # Calculate the scaling factor to fit within the maximum dimensions
            width, height = res_img.size
            if width > max_width or height > max_height:
                res_img.thumbnail((max_width, max_height), PIL.Image.Resampling.LANCZOS)

                # Save the resized image back to the same field
                output = BytesIO()
                res_img.save(output, format='PNG', quality=75) #maintains the quality of transparency
                output.seek(0)
                self.product_image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.product_image.name.split('.')[0], 'image/png', sys.getsizeof(output), None)
        
        super().save(*args, **kwargs)

    #returns product name
    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = 'Product Items'

# ----- BCH Products Transaction records -----
class ProductTransactions(models.Model):
    bch_value = models.FloatField(default=0, null=True)
    tx_hash = models.CharField(max_length = 256, null=True)
    recipient = models.CharField(max_length = 256, null=True)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    product_code = models.CharField(max_length = 3, null=True)
    product_quantity = models.IntegerField(default=0, null=True)
    item_hash =  models.CharField(max_length = 256, null=True)
    total_paid = models.FloatField(default=0, null=True)
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(null=True)
    paid_timestamp = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # --- Overriding the save function for hashing transactions ---
    def save(self, *args, **kwargs): 
        if not self.item_hash:
            self.item_hash = self.generate_hash()
        super().save(*args, **kwargs)

    #generates hash inputs based on the fields mentions from the ProductItems table
    def generate_hash(self):
        #hash_input = f'{self.product_item.product_name}{self.product_item.product_price}{self.product_item.product_quantity}{self.product_item.product_code}'
        hash_input = uuid.uuid4().hex #revised the item_hashing
        return hashlib.sha256(hash_input.encode()).hexdigest()
    
    #returns a string for the hashed transaction and the product name
    def __str__(self):
        return f'Transaction {self.item_hash} for {self.product_item.product_name}'
    
    class Meta:
        verbose_name_plural = 'Product Transactions'

# ----- Selling BitCoin Cash records -----
class BchSellTransaction(models.Model):
    tx_id = models.CharField(max_length = 64, null=True) 
    sender_address = models.CharField(max_length = 64, null=True)
    destination_address = models.CharField(max_length = 64, null=True)
    cash_amount = models.IntegerField(null=True)
    cash_minus_fee_amount = models.FloatField(default=0)
    bch_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_status = models.BooleanField(default=False)

    def __str__(self):
     return self.tx_id

    class Meta:
        verbose_name_plural = 'BCH Sell Transactions'   