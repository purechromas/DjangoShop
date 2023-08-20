from django.db import models

from users.models import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='category', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)
