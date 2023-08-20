from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    is_verified = models.BooleanField(default=False, verbose_name='верификация')
    phone = models.IntegerField(unique=True, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatar/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
