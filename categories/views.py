from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from categories.forms import CategoryCreateForm
from categories.models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {'title': 'Categories'}


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('categories:category_list')
    extra_context = {'title': 'Create Category'}
