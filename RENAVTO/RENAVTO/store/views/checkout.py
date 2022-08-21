from django.shortcuts import render
from django.views import View

from ..models.product import Auto_part
from ..models.order import QuickOrder, Order
from ..templatetags.cart import total_cart_price, total_cart_quantity


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

def nova_post(request):
    return render(request, "checkout.html")