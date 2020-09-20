from django import forms

from category.models import Category
from product.models import Product


def choices():
    queryset = Category.objects.all()
    context = []
    for qs in queryset:
        var = (qs.pk, qs.name)
        context.append(var)
    return context


class CreateProductForm(forms.Form):

    name = forms.CharField(max_length=32)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    category = forms.ChoiceField(choices=choices())

    def clean(self):
        pk = int(self.cleaned_data['category'])
        category = Category.objects.filter(pk=pk).first()
        self.cleaned_data['category'] = category

    def save(self):
        product = Product.objects.create(**self.cleaned_data)

