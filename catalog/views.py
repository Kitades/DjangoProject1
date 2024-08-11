from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, '
              f'{phone}, '
              f'{message} ')

    return render(request, 'contacts.html')


def base(request):
    products = Product.objects.all()
    context = {'base': products}
    return render(request, 'product_list.html', context)


def base_product(request, pk):
    product = Product.objects.get(pk=pk)
    """
        get_object_or_404(Product, pk=pk) вместо Product.objects.get
        выдаст -- Page not found -- если id нет а не ошибку
    """
    context = {'base': product}
    return render(request, 'base_product.html', context)
