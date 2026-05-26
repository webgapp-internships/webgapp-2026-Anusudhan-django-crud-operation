from django.shortcuts import render
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

def formedit(request):
    return render(request,"formedit.html")             

#create your views here.
