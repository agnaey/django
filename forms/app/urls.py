from django.urls import path
from . import views

urlpatterns=[

    path('',views.normal_form_fun)
]