from django.shortcuts import render,redirect,get_object_or_404
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

def detail(request,id):
    prod = get_object_or_404(Product,ProductId=id)
    return render(request,'myapp/detail.html',{'prod':prod})

def edit(request,id):
    prod = get_object_or_404(Product,ProductId=id)
    form = ProductForm(instance=prod)
    if request.method=="POST":
        form = ProductForm(request.POST,instance=prod)
        form.save()
        return redirect("/")
    return render(request,'myapp/edit.html',{'form':form})

def delete(request,id):
    prod = get_object_or_404(Product,ProductId=id)
    return render(request,'myapp/delete.html',{'prod':prod})


