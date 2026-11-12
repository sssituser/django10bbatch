from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>Home</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align:center;color:red'>Regsiter</h1>")

def login(request):
    return HttpResponse("<h1 style='text-align:center;color:blue'>Login</h1>")

def about(request):
    return HttpResponse("<h1 style='text-align:center;color:red'>About</h1>")

def contact(request):
    return HttpResponse("<h1 style='text-align:center;color:green'>Contact</h1>")