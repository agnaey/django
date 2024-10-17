from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("Hello World!")
def fun2(req,a, b, c):                  ##greatest
    if a>b and a>c:
        return HttpResponse(a)
    elif b > a and b > c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)

def index_page(request):
    return render(request, 'index.html')         ##html

def fun3(request,salary,yearofservice):
    if yearofservice>5:
        salary*0.05
        total=(0.05* salary)+salary
        return HttpResponse("you are eligible ",total)
    else:
        return HttpResponse("you are not eligible")


