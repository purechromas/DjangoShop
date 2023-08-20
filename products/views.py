from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from products.forms import ProductForm, ProductVersionForm
from products.models import Product, ProductVersion


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Products'}

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        queryset = Product.objects.filter(category=category_id)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Create product'}

    def get_success_url(self):
        category_id = self.request.POST.get('category')
        success_url = reverse_lazy('products:product', kwargs={'pk': category_id})
        return success_url

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {'title': 'Update product'}

    def get_success_url(self):
        return reverse('products:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_version_formset = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)

        if self.request.method == 'POST':
            formset = product_version_formset(self.request.POST, instance=self.object)
        else:
            formset = product_version_formset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('categories:category_list')


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Product'}
