from django.urls import  path
from myapp import views

urlpatterns=[
    path('',views.getproducts),
    path('register/',views.signup),
    path('edit/<int:id>/',views.edit),
    path('detail/<int:id>/',views.detail),
    path('delete/<int:id>/',views.delete),
]