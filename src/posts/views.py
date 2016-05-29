from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_home(request):
    return HttpResponse("<h1>hello</h1>")

def post_get(request):

    id = int(request.GET.get('id'))
    context = {
        "id": id
    }
    return render(request, "contact.html", context)

def post_reg(request,id=10,foo='me'):

    #id = int(request.GET.get('id'))
    context = {
        "id": id,
        "foo":foo
    }
    return render(request, "contact.html", context)