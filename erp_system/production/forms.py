from django import forms
from .models import Production

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['product_name', 'product_quantity', 'product_date']

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')
        if not product_name:
            raise forms.ValidationError('This field cannot be blank.')
        return product_name

    def clean_product_quantity(self):
        product_quantity = self.cleaned_data.get('product_quantity')
        if not product_quantity:
            raise forms.ValidationError('This field cannot be blank.')
        return product_quantity

    def clean_product_date(self):
        product_date = self.cleaned_data.get('product_date')
        if not product_date:
            raise forms.ValidationError('This field cannot be blank.')
        return product_date