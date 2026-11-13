from django.shortcuts import render

# Create your views here.
def home(request):
    empdict={
        "eid":111,
        "ename":"Pranaya",
        "esal":50000
    }
    return render(request,'myapp/home.html',empdict)

def register(request):
    studict ={
        "sid":123,
        "sname":"Kiran kumar",
        "smarks":650
    }
    return render(request,'myapp/register.html',studict)