from .models import Auto_part, Brand_of_car, Model_of_car, Type_of_part, Part_category


def parts_for_cart(request):
    print(type(request.session.get('cart')))
    if request.session.get('cart'):
        ids = list(request.session.get('cart').keys())
        return {"parts_for_cart": Auto_part.get_products_by_id(ids), "is_the_cart":True}
    else :
        return {"is_the_cart": False}
def left_filter(request):
    return {"brands_filt":Brand_of_car.lst_of_all_brands.all(),
            'models_filt':Model_of_car.lst_of_all_models.all(),
            'types_filt':Type_of_part.objects.all(),
            'categories_filt':Part_category.lst_of_all_categories.all()}
def top_product(request):
    return {'top_products':Auto_part.lst_of_all_parts.filter(top_product=True)}
