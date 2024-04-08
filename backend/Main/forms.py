from django import forms
from .models import *

# Will handle all types of forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ('__all__')

    def clean_product_code(self):
        product_code = self.cleaned_data.get('product_code') #gets entry from any products

        #will filter product codes that already have an entry
        if ProductItem.objects.filter(product_code=product_code).exists():
            raise forms.ValidationError("A product with this code already exist, please try your entry with a different product code.")
        return product_code
    
class VendoRegForm(forms.ModelForm):
    class Meta:
        model = VendoRegistration
        fields = ('__all__')