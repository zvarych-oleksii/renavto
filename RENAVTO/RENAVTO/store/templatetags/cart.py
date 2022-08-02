from django import template
import datetime
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False
@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;
@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * cart_quantity(product , cart)


@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p , cart)

    return sum
@register.filter(name='total_cart_quantity')
def total_cart_quantity(products , cart):
    sum = 0 ;
    for p in products:
        sum += cart_quantity(p , cart)
    return sum
@register.filter(name="is_product_new")
def is_product_new(date):
    date1 = date.date_create
    date2 = datetime.datetime.today()
    print((date1 - date2.date()).days)
    if abs((date1-date2.date()).days)<=7:
        return True
    else:
        return False
