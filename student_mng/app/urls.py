from django.urls import path
from . import views

urlpatterns=[
    path('index',views.index_page),
    path('add',views.add_std),
    path('disp',views.disp_std),
    path('edit/<id>',views.edit_std)


]