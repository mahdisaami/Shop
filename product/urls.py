from django.urls import path

from product.views import CreateProductView, add_product, ProductListView, ProductDetailView, StarView

urlpatterns = [
    path('add/product/', add_product, name='add_product'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/star/<int:pk>', StarView.as_view(), name='star'),
]