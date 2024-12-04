from django.shortcuts import render,redirect
from . forms import *
from .models import *
# Create your views here.

def normal_form_fun(req):
    if req.method=='POST':
        form1=normal_form(req.POST)
        if form1.is_valid():
            roll_no=form1.cleaned_data['roll_no']
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            data=student.objects.create(roll_no=roll_no,name=name,age=age)
            data.save()
            return redirect(normal_form_fun)

    form=normal_form()
    return render(req,'normal_form.html',{'form':form})


def model_form_fun(req):
    if req.method=='POST':
        form1=model_form(req.POST)
        if form1.is_valid():
            form1.save()
            return redirect(model_form_fun)
    form=model_form()
    return render(req,'model_form.html',{'form':form})


