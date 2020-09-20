from django.urls import path

from product.views import CreateProductView

urlpatterns = [
    path('add/product/', CreateProductView.as_view(), name='create_product'),
]