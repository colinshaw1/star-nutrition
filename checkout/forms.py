from djanjo import forms
from .models import Order

# class for the order form
class OrderForm(forms.ModelForm):
    class Meta:
        # tells danjo which model is assoicated ot the form
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)