from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from products.apps import ProductsConfig
from products.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = ProductsConfig.name

urlpatterns = [
    path('<int:pk>', ProductListView.as_view(), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
]
