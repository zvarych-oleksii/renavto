from django.shortcuts import render
from django.template.defaultfilters import upper

from ..models import Auto_part


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
    return render(request, "../templates/search_results.html", {"search_results": q})