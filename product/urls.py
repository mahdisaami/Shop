from django.urls import path

from product.views import CreateProductView, create_product, ProductListView, ProductDetailView, StarView

urlpatterns = [
    path('create/product/', create_product, name='create_product'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/star/<int:pk>', StarView.as_view(), name='star'),
]