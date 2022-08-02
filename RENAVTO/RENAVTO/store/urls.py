
from django.contrib import admin
from django.urls import path
from .views import Index, PartList, AutoPartDetail, models, types, category, qet_queryset,nova_post,CheckOut,SideFilter

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('filter/', SideFilter.as_view(), name="side_filter"),
    path('store/<slug:brand>/', models),
    path('store/<slug:brand>/<str:model>/', types, ),
    path('store/<slug:brand>/<str:model>/<str:type>/', category, name="filtered_categories"),
    path('store/<slug:brand>/<str:model>/<str:type>/<str:category>/', PartList.as_view(), name="filtered_parts"),
    path('d', qet_queryset, name='search'),
    path('part/', AutoPartDetail.as_view(), name='Auto_part_det'),
    path('part/<int:pk>', AutoPartDetail.as_view(), name='Auto_part_det'),
    path('checkout/', nova_post, name='checkout'),
    path('successful/', CheckOut.as_view(), name='successful'),
]