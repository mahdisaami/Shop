from django.urls import path

from product.views import CreateProductView, add_product, ProductListView

urlpatterns = [
    # path('add/product/', CreateProductView.as_view(), name='create_product'),
    path('add/product/', add_product, name='add_product'),
    path('products/', ProductListView.as_view(), name='product_list')
]