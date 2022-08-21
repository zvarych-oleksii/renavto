from django.shortcuts import redirect
from django.views.generic import DetailView

from ..models import Auto_part


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
