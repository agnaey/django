from django.shortcuts import render
from . models import *

# Create your views here.

def index_page(request):
    data=movie.objects.all()[:4]
    data1=movie.objects.all()[4:9]
    return render(request, 'index.html',{'data':data,'data1':data1})

def secpage(request,id):
    data=movie.objects.get(pk=id)
    member=members.objects.filter(movie=data)


    data1=movie.objects.all()[:4]
    data2=movie.objects.all()[4:9]
    return render(request, 'secpage.html',{'data':data,'member':member,'data1':data1,'data2':data2,})

