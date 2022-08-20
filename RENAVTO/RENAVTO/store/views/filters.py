from django.shortcuts import redirect, render
from django.views import View

from ..models import *


class SideFilter(View):
    def post(self, request):
        brand_for_filter = str(request.POST.get('brand'))
        model_for_filter = str(request.POST.get('model'))
        type_for_filter = str(request.POST.get('type'))
        category_for_filter = str(request.POST.get('category'))
        url_str = '/store'
        url_str = url_str + '/' + brand_for_filter + '/' + model_for_filter + '/' + type_for_filter + '/' + category_for_filter
        return redirect(url_str)
def models(request, brand):
    car_brand = Brand_of_car.lst_of_all_brands.get(name_of_brand = brand)
    car_models = Model_of_car.lst_of_all_models.filter(model_of_car=car_brand)
    return render(request, 'car_models.html', {'car_models': car_models})
def types(request, brand, model):
    part_types = Type_of_part.objects.all()
    return render(request, 'part_type.html', {'part_types':part_types})
def category(request, brand, model, type):
    part_type = Type_of_part.objects.get(name_of_type = type)
    part_category = Part_category.lst_of_all_categories.filter(part_category =part_type)
    return render(request, 'part_category.html', {'part_category':part_category})
