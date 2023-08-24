from django.urls import path

from categories.apps import CategoriesConfig
from categories.views import CategoryCreateView, category_list_view

app_name = CategoriesConfig.name

urlpatterns = [
    path('', category_list_view, name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
