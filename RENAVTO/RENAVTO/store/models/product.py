import datetime

from django.db import  models
from .categories import Brand_of_car, Model_of_car, Type_of_part, Part_category
class Auto_part(models.Model):
    lst_of_all_parts = models.Manager()
    name = models.CharField(blank=False, max_length=70)
    price = models.IntegerField(default=0, blank=False)
    description = models.CharField(blank=True, max_length=200)
    produced_by = models.CharField(blank=False, verbose_name="Виробник:", max_length=70)
    serial_number = models.CharField(blank=False, max_length=30)
    image = models.ImageField(upload_to='products/', blank=False)
    state = models.BooleanField("Стан B/Y", default=False)
    top_product = models.BooleanField("Найпопулярніші товари", default=False)
    car_brand = models.ForeignKey(
        Brand_of_car, verbose_name="Марка", on_delete=models.SET_NULL, null=True
    )
    car_model = models.ForeignKey(
        Model_of_car, verbose_name="Модель", on_delete=models.SET_NULL, null=True
    )
    part_type = models.ForeignKey(
        Type_of_part, verbose_name="Тип", on_delete=models.SET_NULL, null=True
    )
    part_category = models.ForeignKey(
        Part_category, verbose_name="Під тип", on_delete=models.SET_NULL, null=True
    )
    date_create = models.DateField(verbose_name="Останній раз змінено:",default=datetime.datetime.today)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Запчастини'
        verbose_name = 'Запчастина'
        ordering = ['name']

    @staticmethod
    def get_products_by_id(ids):
        return Auto_part.lst_of_all_parts.filter(id__in = ids)