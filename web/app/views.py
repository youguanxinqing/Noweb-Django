from django.shortcuts import render
from django.http import (
    HttpResponse
)

# Create your views here.

def index(request):
    return HttpResponse("Welcome to App Index !")

def greet_someone(request, name):
    """
    位置传参(url)
    
    url: http://0.0.0.0/app/zhong/
    res: Hello zhong.
    """
    return HttpResponse(f"Hello {name}.")
