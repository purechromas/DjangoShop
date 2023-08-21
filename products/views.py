from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from products.forms import ProductVersionForm, ProductUserForm, ProductModeratorForm
from products.models import Product, ProductVersion


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {'title': 'Products'}

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        user = self.request.user

        if user.groups.filter(name='moderator').exists():
            queryset = Product.objects.all()
        else:
            queryset = Product.objects.filter(category=category_id, user=user, is_published=True)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductUserForm
    extra_context = {'title': 'Create product'}

    def get_success_url(self):
        category_id = self.request.POST.get('category')
        success_url = reverse_lazy('products:product', kwargs={'pk': category_id})
        return success_url

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    extra_context = {'title': 'Update product'}
    permission_required = 'products.change_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

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

    def get_form_class(self):
        if self.request.user.groups.filter(name='Users').exists():
            return ProductUserForm
        elif self.request.user.groups.filter(name='moderator').exists():
            return ProductModeratorForm
        else:
            raise ValueError("No appropriate form found for this user")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('categories:category_list')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    extra_context = {'title': 'Product'}
