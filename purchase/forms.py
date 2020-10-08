from django import forms
from django.core.exceptions import ValidationError

from purchase.models import BasketProduct, Basket


class CreateBasketProductForm(forms.ModelForm):

    class Meta:
        model = BasketProduct
        fields = ('product', 'quantity')

    def clean(self):
        if self.cleaned_data['quantity'] > 3:
            raise ValidationError('More than 3 is not allowed')
        return self.cleaned_data

    def save(self, commit=True):
        self.instance.price = self.instance.product.price
        return super(CreateBasketProductForm, self).save(commit=commit)


class RetrieveBasketForm(forms.ModelForm):

    class Meta:
        model = Basket
        fields = ('products',)