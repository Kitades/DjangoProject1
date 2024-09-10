from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    description = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    description = models.CharField(max_length=100, verbose_name="Описание")
    imagen = models.ImageField(
        upload_to="imagen/preview", verbose_name="Превью", null=True, blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(verbose_name="Дата создания")
    updated_at = models.DateTimeField(verbose_name="Дата изменения")
    # manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта', null=True, blank=True)

    def __str__(self):
        return (
            f"{self.name}, {self.description}, {self.imagen}, {self.category}, {self.price}, "
            f"{self.created_at}, {self.updated_at}"
        )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "price",
            "category",
        ]
