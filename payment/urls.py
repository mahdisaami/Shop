from django.urls import path

from payment.views import CreateInvoice, RetrieveInvoice

urlpatterns = [
    path('create/invoice/', CreateInvoice.as_view(), name='create_invoice'),
    path('invoice/<int:pk>/', RetrieveInvoice.as_view(), name='retrieve_invoice')
]