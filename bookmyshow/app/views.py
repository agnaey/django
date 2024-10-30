from django.shortcuts import render
# from . import views

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def armpage(request):
    return render(request, 'armpage.html')

