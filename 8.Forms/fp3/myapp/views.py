from django.shortcuts import render,redirect
from myapp.forms import ProductForm
from myapp.models import Product
# Create your views here.
def signup(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'myapp/register.html',{'form':form})

def getproducts(request):
    prods = Product.objects.all()
    return render(request,'myapp/products.html',{'prods':prods})