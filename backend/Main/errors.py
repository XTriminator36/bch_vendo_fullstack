#will handle all the errors of this app
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product, ProductItem
import models

#errors for quantity check
@receiver(pre_save, sender=ProductItem)
def check_product_item_limit(sender, instance, **kwargs):

    #gets the product code of the product item
    product_code = instance.product.code

    #gets the maximum quantity allowed for this particular product code
    max_quantity = Product.objects.get(code=product_code).max_quantity

    #gets the total quantity of product items with this praticular product code 
    total_quantity = ProductItem.objects.filter(product__code=product_code).aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0

    #check if adding the new item will exceed the maximum limit
    if total_quantity + instance.quantity > max_quantity:
        raise ValueError(f"Exceeds maximun quantity for this particular product {product_code}")
    
#other error handles here.....


