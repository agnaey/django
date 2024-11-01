from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from . models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user'in req.session:
        return redirect(user_home)
    else:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname
                    return redirect(shop_home)
                else:
                    req.session['user']=uname
                    return redirect(user_home)
            else:
                messages.warning(req, "username or password invalid.") 
            return redirect(shop_login)
        else:
            return render(req,'login.html')
    
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
            return redirect(shop_login)
        except:
            messages.warning(req,'user details already exits') 
            return redirect(register)   
    else:
        return render(req,'register.html')

# ----------------------------admin----------------------------------


def shop_home(req):
    if 'shop' in req.session:
        products=product.objects.all()
        return render(req,'shop/shop_home.html',{'products':products})
    else:
       return redirect(shop_home)
    
def add_product(req):
    if req.method=='POST':
        id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST['o_price']
        file=req.FILES['img']
        data=product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,img=file)
        data.save()
        return redirect(shop_home)

    return render (req,'shop/add_pro.html')

def edit_pro(req,id):
    pro=product.objects.get(pk=id)
    if req.method=='POST':
        e_id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST['o_price']
        file=req.FILES.get('img')
        print(file)
        if file:
            product.objects.filter(pk=id).update(pro_id=e_id,name=name,price=price,offer_price=offer_price,img=file)
        else:
            product.objects.filter(pk=id).update(pro_id=e_id,name=name,price=price,offer_price=offer_price)
        return redirect(shop_home)
    return render(req,'shop/edit_pro.html',{'data':pro})

def delete_pro(req,id):
    data=product.objects.get(pk=id)
    url=data.img.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(shop_home)

# -------------------------------user------------------

def user_home(req):
    if 'user' in req.session:
        products=product.objects.all()
        return render(req,'user/user_home.html',{'products':products})

def view_product(req,id):
        products=product.objects.get(pk=id)
        return render(req,'user/view_pro.html',{'products':products})

def add_to_cart(req,pid):
    products=product.objects.get(pk=pid)
    print(products)
    user=User.objects.get(username=req.session['user'])
    print(user)
    data=Cart.objects.create(user=user,products=products)
    data.save()
    return redirect(cart_display)

def cart_display(req):
    return render(req,'cart_display.html')



