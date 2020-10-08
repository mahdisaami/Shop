from django.urls import path

from purchase.views import CreateBasketProduct, AddProduct, RetrieveBasket

urlpatterns = [
    path('add/product/form/', CreateBasketProduct.as_view(), name='add_product_form'),
    path('add/product/<int:pk>/', AddProduct.as_view(), name='add_product'),
    path('basket/', RetrieveBasket.as_view(), name='retrieve_basket'),
]
