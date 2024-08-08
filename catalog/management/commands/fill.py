from django.core.management import BaseCommand

from catalog.models import Category, Product

import os
from config.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        fix_data = ('data_catalog.json', 'data_product.json')
        for fd in fix_data:
            cmd = f'python3 manage.py loaddata {BASE_DIR}/{fd}'
            os.system(cmd)


