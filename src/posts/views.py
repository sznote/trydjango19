from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_home():
    return HttpResponse("<h1>hello</h1>")
