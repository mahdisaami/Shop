from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from category.models import Category
from product.models import Product, Media, PrAttribute


def choices():
    queryset = Category.objects.all()
    context = []
    for qs in queryset:
        var = (qs.pk, qs.name)
        context.append(var)
    return context


class CreateProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(is_parent=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'


class ImageForm(forms.ModelForm):
    media_file = forms.ImageField(label='Image')

    class Meta:
        model = Media
        fields = ('media_file',)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'


class CreatePrAttribute(forms.ModelForm):
    value = forms.CharField(label='Value:',)

    class Meta:
        model = PrAttribute
        fields = ('value',)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'
