from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("this is contact")


def track(request):
    return HttpResponse("this is track")


def prodview(request):
    return HttpResponse("this is prodview")


def checkout(request):
    return HttpResponse("this is checkout")