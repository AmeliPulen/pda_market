from django.db import models
from django.utils import timezone

from config import settings


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    # created_at = models.DateTimeField(++NULLABLE, default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    price = models.FloatField(default=0, verbose_name='Цена за штуку')
    overview = models.TextField(**NULLABLE, verbose_name='Описание')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price',)


