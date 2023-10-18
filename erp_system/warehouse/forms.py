from django import forms
from .models import Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['product', 'quantity', 'location']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError('Quantity cannot be negative.')
        return quantity

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location:
            raise forms.ValidationError('Location is required.')
        return location