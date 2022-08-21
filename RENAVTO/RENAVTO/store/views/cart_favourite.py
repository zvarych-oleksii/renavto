from django.shortcuts import redirect, render

from ..models import Auto_part


def cart_header(request):
    cart = request.session['cart']
    cart = cart.keys
    parts_example = Auto_part.lst_of_all_parts.all()
    return render(request, 'base/header.html', {'parts_example':parts_example})

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