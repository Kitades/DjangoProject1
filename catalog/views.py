from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, SubjectForm
from catalog.models import Product, Subject


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, '
              f'{phone}, '
              f'{message} ')

    return render(request, 'catalog/contacts.html')


class CatalogListView(ListView):  # app_name/<model_name>_<action> --> catalog/product_list
    model = Product


class CatalogDetailView(DetailView):
    model = Product


class CatalogProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Subject, form=SubjectForm, extra=1)
        context_data['formset'] = SubjectFormset()
        return context_data
