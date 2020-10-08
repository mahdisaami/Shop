from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from payment.models import Invoice
from purchase.models import Basket


class CreateInvoice(View):

    def get(self, request, *args, **kwargs):
        basket = Basket.objects.filter(user=request.user, paid=False).first()
        price = basket.total_price()
        invoice = Invoice.objects.filter(basket=basket, user=request.user, paid=False).first()
        if invoice is None:
            invoice = Invoice.objects.create(basket=basket, user=request.user, paid=False, price=price)
            return redirect('/invoice/{}/'.format(invoice.pk))
        invoice.price = price
        invoice.save()
        return redirect('/invoice/{}/'.format(invoice.pk))


class RetrieveInvoice(DetailView):
    model = Invoice
    template_name = 'payment/retrieve_invoice.html'
