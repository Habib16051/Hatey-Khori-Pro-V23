from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_category', 'product_name', 'product_price', 'product_description', 'product_image']

    # You can add additional validation or custom form fields here if needed.
    
# Contact Form Validation
class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

