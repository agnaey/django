from django.shortcuts import render
from django.http import HttpResponse
from . models import Students

# Create your views here.

def index_page(request):
    data=Students.objects.all()
    return render(request, 'index.html',{'data':data})

def add_std(req):
    return render(req,'add.html')


