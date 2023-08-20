from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='заголовок')
    slug = models.SlugField(verbose_name='силка-slug')
    contained = models.TextField(verbose_name='содержимое')
    preview_image = models.ImageField(upload_to='blog/', verbose_name='изображение')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
