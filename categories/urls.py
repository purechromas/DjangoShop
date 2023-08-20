from django.urls import path

from categories.apps import CategoriesConfig
from categories.views import CategoryListView, CategoryCreateView

app_name = CategoriesConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
