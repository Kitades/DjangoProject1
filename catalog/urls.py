from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, base, base_product
from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', base, name='base'),
    path('base/<int:pk>', base_product, name='base')
]
