from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView
from catalog.views import contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', CatalogListView.as_view(), name='list'),
    path('detail/<int:pk>', CatalogDetailView.as_view(), name='detail'),
]
