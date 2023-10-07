from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product, ProductCategory
from .forms import ProductForm
from django.urls import reverse_lazy  # Required for DeleteView


class HomeView(TemplateView):
    template_name = 'home.html'
    
class ProductListView(ListView):
    model = Product
    template_name = 'm_shop/shop.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'm_shop/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'm_shop/add_product.html'

    def form_valid(self, form):
        product = form.save()
        return redirect('product_detail', pk=product.pk)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'm_shop/update_product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'm_shop/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('shop')

class ManageCategoriesView(ListView):
    model = ProductCategory
    template_name = 'm_shop/manage_categories.html'
    context_object_name = 'categories'
