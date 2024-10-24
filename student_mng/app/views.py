from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Students

# Create your views here.

def index_page(request):
    data=Students.objects.all()
    return render(request, 'index.html',{'data':data})

def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll']
        std_name=req.POST['name']
        std_age=req.POST['age']
        std_email=req.POST['email']
        std_phone=req.POST['phone']
        data=Students.objects.create(roll_no=roll,name=std_name,age=std_age,email=std_email,phone=std_phone)
        data.save()
        return redirect(disp_std)
    else:
        return render(req,'add.html')

def disp_std(req):
    data=Students.objects.all()
    return render(req,'display_std.html',{'data':data})

def edit_std(req,id):
    data=Students.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST['roll']
        std_name=req.POST['name']
        std_age=req.POST['age']
        std_email=req.POST['email']
        std_phone=req.POST['phone']
        Students.objects.filter(pk=id).update(roll_no=roll,name=std_name,age=std_age,email=std_email,phone=std_phone)
        return redirect(disp_std)
    else:
        return render(req,'edit_std.html',{'data':data})


