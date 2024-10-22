from django.shortcuts import render,redirect
from django.http import HttpResponse
todo=[{'id':'1','task':'task1'},{'id':'2','task':'task2'}]

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
    name='agnaey'
    age=21
    place='knr'
    return render(request, 'index.html',{'name':name,'age':age,'place':place})         ##html



def fun3(request,salary,yearofservice):         ##work1
    if yearofservice>5:
        salary*0.05
        total=(0.05* salary)+salary
        return HttpResponse("you are eligible ",total)
    else:
        return HttpResponse("you are not eligible")
    
def demo_page(req):
    # l=[1,2,3,4,5,6,7]
    # l={'name':'agnaey','age':21,'place':'knr'}
    l=[{'name':'agnaey','age':21,'place':'knr'},{'name':'akshay','age':20,'place':'knr'},{'name':'kartik','age':21,'place':'koz'}]
    d={'name':'akshay','age':20,'place':'knr'}
    return render(req,'demo.html',{'data':l,'data1':d})

def sec_page(req):
    return render(req,'second.html')

def todo_page(req):
    if req.method=='POST':
        id=req.POST['id']
        task=req.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(todo_page)
    return render (req,'todo.html',{'todo':todo})

def edit_page(req,id):
    task=''
    for i in todo:
        if i['id']==id:
            task=i
    if req.method=='POST':
        id=req.POST['id']
        task1=req.POST['task']
        task['id']=id
        task['task']=task1
        return redirect (todo_page)

    return render(req,'edit.html',{'task':task})

def delete_fun(req,id):
    for i in todo:
        if i['id']==id:
            todo.remove(i)
    return redirect(todo_page)
    


