from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, FormView, DetailView

from payment.models import Invoice
from product.models import Product
from purchase.forms import CreateBasketProductForm, RetrieveBasketForm
from purchase.models import Basket, BasketProduct


class CreateBasketProduct(CreateView):
    form_class = CreateBasketProductForm
    template_name = 'purchase/create_product_basket.html'
    success_url = 'add_product_form'

    def form_valid(self, form):
        basket, _ = Basket.objects.get_or_create(user=self.request.user)
        product = form.instance.product
        bp = BasketProduct.objects.filter(product=product, basket=basket).first()
        if bp is not None:
            quantity = bp.quantity + form.instance.quantity
            bp.quantity = quantity
            bp.save()
            return redirect('/add/product/form/')

        form.instance.basket = basket
        form.save()
        return super(CreateBasketProduct, self).form_valid(form)


class AddProduct(View):

    def get_object(self):
        obj = Product.objects.filter(pk=self.kwargs['pk']).first()
        return obj

    def get(self, request, *args, **kwargs):
        basket, _ = Basket.objects.get_or_create(user=request.user)
        product = self.get_object()
        price = product.price
        bp = BasketProduct.objects.filter(basket=basket, product=product).first()
        if bp is not None:
            quantity = bp.quantity + 1
            bp.quantity = quantity
            bp.save()
            messages.success(request, 'Added to your basket')
            return redirect('/product/{}'.format(self.kwargs['pk']))
        basket_product = BasketProduct.objects.create(basket=basket, product=product, quantity=1, price=price)
        messages.success(request, 'Added to your basket')
        return redirect('/product/{}'.format(self.kwargs['pk']))


class RetrieveBasket(DetailView):
    model = Basket
    template_name = 'purchase/retrieve_basket.html'

    def get_object(self):
        obj = Basket.objects.filter(user=self.request.user).first()
        return obj
