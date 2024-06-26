from django.db import models

from django.urls import reverse


class Brand_of_car(models.Model):
    img_of_brand = models.FileField(verbose_name='Фото моделі', upload_to='brands_images/')
    name_of_brand = models.CharField(max_length=25, verbose_name='brand name')
    lst_of_all_brands = models.Manager()
    def __str__(self):
        return self.name_of_brand

    class Meta:
        verbose_name_plural = 'Марки автомобілів'
        verbose_name = 'Марка автомобіля'
        ordering = ['name_of_brand']
class Model_of_car(models.Model):
    img_of_model = models.FileField(verbose_name='Фото моделі', upload_to='models_images/')
    model_of_car = models.ForeignKey(
        Brand_of_car, on_delete=models.CASCADE, verbose_name='Model')
    name_of_model = models.CharField(max_length=25, unique=True, verbose_name='Model name')
    lst_of_all_models = models.Manager()
    def __str__(self):
        return self.name_of_model

    class Meta:
        verbose_name_plural = 'Моделі автомобілів'
        verbose_name = 'Модель автомобіля'
        ordering = ['name_of_model']

class Type_of_part(models.Model):
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    img_of_type = models.FileField(verbose_name='Example image', upload_to='type_example_images/')
    name_of_type = models.CharField(max_length=25, verbose_name='Type name')
    def __str__(self):
        return self.name_of_type

    class Meta:
        verbose_name_plural = 'Типи запчастин'
        verbose_name = 'Тип запчастини'
        ordering = ['name_of_type']


class Part_category(models.Model):
    part_category = models.ForeignKey(Type_of_part, on_delete=models.CASCADE, verbose_name='Category')
    name_of_category = models.CharField(max_length=25, unique=True, verbose_name='Name of category')
    img_of_category = models.FileField(verbose_name='Фото категорій запчастин', upload_to='category_images/')
    lst_of_all_categories = models.Manager()
    def __str__(self):
        return self.name_of_category

    class Meta:
        verbose_name_plural = 'Категорії'
        verbose_name = 'Категорія'
        ordering = ['name_of_category']

