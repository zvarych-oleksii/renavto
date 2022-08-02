from django.db import models
from .product import Auto_part
import datetime

class Order(models.Model):
    first_name = models.CharField(verbose_name="Ім'я:",max_length=30, blank=False)
    second_name = models.CharField(verbose_name="Прізвище:",max_length=30, blank=False)
    city = models.CharField(verbose_name="Місто:",max_length=30, blank=False)
    nova_post_number = models.CharField(verbose_name="Номер нової пошти:",max_length=30, blank=False)
    oplata_on_post = models.BooleanField(verbose_name="Оплата у відділенні:",default=True)
    date_of_order = models.DateField(verbose_name="Коли було зроблене замовлення:",default=datetime.datetime.today)
    quantity_total = models.IntegerField(verbose_name="Кількість всіх товарів:")
    price_total = models.IntegerField(verbose_name="Ціна замовлення:")
    phone_number = models.CharField(verbose_name="Номер телефону:",blank=False, max_length=15)
    product = models.TextField(verbose_name="Замовлені запчастини:",blank=False)

    def placeOrder(self):
        self.save()