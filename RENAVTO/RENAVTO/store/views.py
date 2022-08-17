from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from requests import post, get
import json
from django.template.defaultfilters import upper
from django.views import View
from .models.product import Auto_part
from .models.categories import Model_of_car,Brand_of_car,Type_of_part,Part_category
from .models.order import Order, QuickOrder
from .templatetags.cart import total_cart_price, total_cart_quantity, cart_quantity, price_total

class Index(TemplateView):
    template_name = "index.html"
    def post(self , request):
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
        return redirect("index")


class SideFilter(View):
    def post(self, request):
        brand_for_filter = str(request.POST.get('brand'))
        model_for_filter = str(request.POST.get('model'))
        type_for_filter = str(request.POST.get('type'))
        category_for_filter = str(request.POST.get('category'))
        url_str = '/store'
        url_str = url_str + '/' + brand_for_filter + '/' + model_for_filter + '/' + type_for_filter + '/' + category_for_filter
        return redirect(url_str)
class CheckOut(View):
    template_name = 'successful.html'
    def post(self, request):
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get("city")
        nova_poshta = request.POST.get("nova_poshta")
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        products = Auto_part.get_products_by_id(ids)
        parts_str = ''
        for product in products:
            parts_str = parts_str + product.name + ' '+ ' ' + str(cart[str(product.id)])+ ' ' + product.serial_number + " " + str(product.price) + "грн.;\n"
        order = Order(first_name=first_name,
                          second_name=second_name,
                          city=city,
                          nova_post_number=nova_poshta,
                          phone_number=phone_number,
                          product = parts_str,#product,
                          price_total=total_cart_price(products, cart),#product.price,
                          quantity_total=total_cart_quantity(products, cart),#cart.get(str(product.id))
                          );
        order.save()
        request.session['cart'] = {}
        print(request.session.get('cart'))
        return render(request, "successful.html")

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


class AutoPartDetail(DetailView):
    model = Auto_part
    slug_url_kwargs = 'pk'
    template_name = 'auto_part_detail.html'
    context_object_name = 'auto_part'
    def post(self , request, pk):
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
        return redirect('Auto_part_det', pk=pk)

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


def qet_queryset(request):
        value = request.GET.get('sorted_by')
        print(value)
        q = Auto_part.lst_of_all_parts.filter(serial_number=upper(request.GET.get("search_box")))
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        if 'null' in cart.keys():
            del cart['null']
        if None in cart.keys():
            del cart[None]
        request.session['cart'] = cart
        return render(request, "search_results.html", {"search_results": q})
def cart_header(request):
    cart = request.session['cart']
    cart = cart.keys
    parts_example = Auto_part.lst_of_all_parts.all()
    return render(request, 'base/header.html', {'parts_example':parts_example})

def nova_post(request):
    return render(request, "checkout.html")

def add_deadd_something_from_favorite(request):
    product_for_favorite = request.POST.get('product_for_favorite')
    next = request.POST.get('next')
    lst_of_favorites = request.session.get('favorite')
    if lst_of_favorites:
        if product_for_favorite in lst_of_favorites:
            lst_of_favorites.remove(product_for_favorite)
        else:
            lst_of_favorites.append(product_for_favorite)
    else:
        lst_of_favorites = []
        lst_of_favorites.append(product_for_favorite)
    request.session['favorite'] = lst_of_favorites
    return redirect(request.META.get('HTTP_REFERER'))
class QuickCheckOut(View):
    template_name = 'quick_successful.html'
    def post(self, request):
        phone_number = request.POST.get('phone_number')
        id = request.POST.get('auto_part_id')
        product = Auto_part.lst_of_all_parts.get(pk=id)
        parts_str = ''
        parts_str = parts_str + product.name + ' '+ ' ' + product.serial_number + " " + str(product.price) + "грн.;\n"
        quick_order = QuickOrder(
                        phone_number=phone_number,
                          product = parts_str,#product,
                          price_total=Auto_part.lst_of_all_parts.get(pk=id).price
                          );
        quick_order.save()
        return render(request, "quick_successful.html")