from django.shortcuts import redirect
from django.views.generic import ListView

from ..models import *


class ItemsForFilter():
    def get_brands(self, filter_by):
        return Brand_of_car.lst_of_all_brands.get(name_of_brand=filter_by).id
    def get_models(self, filter_by):
        return Model_of_car.lst_of_all_models.get(name_of_model=filter_by).id
    def get_types(self, filter_by):
        return Type_of_part.objects.get(name_of_type=filter_by).id
    def get_category(self, filter_by):
        return Part_category.lst_of_all_categories.get(name_of_category=filter_by).id

class PartList(ListView, ItemsForFilter):
    model = Auto_part
    queryset = Auto_part.lst_of_all_parts.all()
    template_name = 'shop.html'
    def post(self , request, brand, model, type, category):
        print(brand, model, type, category)
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('filtered_parts', brand=brand, model=model, type=type, category=category)
    def get_queryset(self):
        search = self.request.GET.get('order_by')
        brand_car = ItemsForFilter.get_brands(self, self.kwargs['brand'])
        model_car = ItemsForFilter.get_models(self, self.kwargs['model'])
        type_part = ItemsForFilter.get_types(self, self.kwargs['type'])
        category_part = ItemsForFilter.get_category(self, self.kwargs['category'])
        return Auto_part.lst_of_all_parts.filter(car_brand=brand_car, car_model=model_car, part_type=type_part, part_category=category_part)