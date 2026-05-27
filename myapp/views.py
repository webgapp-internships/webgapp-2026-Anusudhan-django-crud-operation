from django.shortcuts import render,redirect
from .models import Forms


def index(request):
    return render(request, "index.html")
def about(request):
    return render(request,"about.html")
def flex(request):
    return render(request,"flex.html")
def  form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age') 
        dob = request.POST.get('dob')
        Forms.objects.create(name = name,age = age,dob = dob)
    return render(request, "form.html") 
    
def formresult(request):
    result=Forms.objects.all()
    return render(request,"formresult.html",{"result":result})

def formedit(request,id):
    edit = Forms.objects.filter(id = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        Forms.objects.filter(id = id).update(name = name,age = age,dob = dob)
    return render(request,"formedit.html",{"edit":edit}) 

def formdelete(request,id):
    delete = Forms.objects.filter(id=id)
    delete.delete()  
    return redirect("formresult")             

#create your views here.
