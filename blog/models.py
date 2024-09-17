from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    slug = models.CharField(max_length=30, verbose_name="Ссылка", null=True, blank=True)
    body = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="imagen/", verbose_name="Изображение", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
