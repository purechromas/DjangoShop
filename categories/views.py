from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from categories.forms import CategoryCreateForm
from categories.models import Category
from categories.services import get_categories_cache


@login_required
def category_list_view(request):
    categories = get_categories_cache()
    return render(request, 'categories/category_list.html', {'categories': categories})


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('categories:category_list')
    extra_context = {'title': 'Create Category'}
