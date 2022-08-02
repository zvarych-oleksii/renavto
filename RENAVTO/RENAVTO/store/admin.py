from django.contrib import admin
from .models.order import Order
from .models.product import Auto_part
from .models.categories import Brand_of_car, Model_of_car, Type_of_part, Part_category

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'serial_number']

admin.site.register(Auto_part, AdminProduct)
admin.site.register(Brand_of_car)
admin.site.register(Model_of_car)
admin.site.register(Type_of_part)
admin.site.register(Part_category)
admin.site.register(Order)
