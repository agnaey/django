from django.urls import path
from . import views

urlpatterns = [
    path('f1', views.fun1),
    path('f2/<int:a>/<int:b>/<int:c>', views.fun2),       ##greatest
    path('index',views.index_page),
    path('work1/<int:salary>/<int:yearofservice>', views.fun3),

]