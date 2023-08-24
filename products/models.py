from django.db import models

from categories.models import Category
from users.models import User, NULLABLE


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='имя')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, verbose_name='категория')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
        permissions = [
            ('moderator', 'moderator_admin'),
        ]


class ProductVersion(models.Model):
    STATUS_CHOICES = [
        (True, 'Актуальная'),
        (False, 'Неактуальная')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='версия')
    version_name = models.CharField(max_length=255, verbose_name='имя версии')
    status = models.BooleanField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0], verbose_name='статус')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продукта'
