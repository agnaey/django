from django.urls import path
from . import views

urlpatterns=[
    path('index',views.index_page),
    path('add',views.add_std),

]