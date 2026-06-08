from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
#request: it is object that contain all the information comming from http response
def home(request):
    return render(request,"home.html")

def form(request):
    return render(request,'form.html')

def login(request):
    return render(request,'login.html')

def card(request):
    data = Product.objects.all()
    return render(request,'cards.html' ,{'data':data})

def calculator(request):
    return render(request,'calculator.html')

def atm(request):
    return render(request,'atm.html')
