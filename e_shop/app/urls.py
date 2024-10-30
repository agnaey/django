from django.urls import path
from . import views

urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),



#  ---------------------admin-------------------   
    path('shop_home',views.shop_home),
    path('add_pro',views.add_product),
    path('edit_pro/<id>',views.edit_pro),





# ----------------------user---------------------------

]