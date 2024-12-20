from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),



#  ---------------------admin-------------------   
    path('shop_home',views.shop_home),
    path('add_pro',views.add_product),
    path('edit_pro/<id>',views.edit_pro),
    path('delete_pro/<id>',views.delete_pro),
    path('register',views.register),
    path('admin_vew_booking',views.admin_view_booking),


# ----------------------user---------------------------
    path('user_home',views.user_home),
    path('view_pro/<id>',views.view_product),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('cart_disp',views.cart_display),
    path('delete_cart/<id>',views.delete_cart),
    path('buy_product/<id>',views.buy_pro),
    path('user_vew_booking',views.user_view_booking),

]