from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        # Строковое отображение объекта
        return f'{self.__class__.__name__}'

    class Meta:
        verbose_name = 'продукт' # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты' # Настройка для наименования набора объектов

class Category(models.Model):
    def __str__(self):
        # Строковое отображение объекта
        return f'{self.__class__.__name__}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов
