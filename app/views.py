from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request: it is object that contain all the information comming from http response
def home(request):
    return render(request,"home.html")

def form(request):
    return render(request,'form.html')

def login(request):
    return render(request,'login.html')

def card(request):
    return render(request,'cards.html')

def calculator(request):
    return render(request,'calculator.html')
