from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def regiser(request):
    return render(request,'myapp/register.html')

def login(request):
    return render(request,'myapp/login.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')