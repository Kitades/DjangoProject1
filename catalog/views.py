from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


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


# def base(request):
#     products = Product.objects.all()
#     context = {'object_list': products}
#     return render(request, 'product_list.html', context)


class CatalogDetailView(DetailView):
    model = Product

# def base_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     """
#         get_object_or_404(Product, pk=pk) вместо Product.objects.get
#         выдаст -- Page not found -- если id нет а не ошибку
#     """
#     context = {'base': product}
#     return render(request, 'catalog/product_detail.html', context)
