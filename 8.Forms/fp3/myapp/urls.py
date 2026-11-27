from django.urls import  path
from myapp import views

urlpatterns=[
    path('',views.getproducts),
    path('register/',views.signup),
]