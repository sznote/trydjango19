from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_create(request):
    return HttpResponse("<h1>created</h1>")


def post_detail(request):
    return HttpResponse("<h1>detail</h1>")


def post_list(request):
    return HttpResponse("<h1>list</h1>")


def post_update(request):
    return HttpResponse("<h1>update</h1>")


def post_delete(request):
    return HttpResponse("<h1>delete</h1>")


def post_home(request):
    return HttpResponse("<h1>home</h1>")


def post_get(request):
    id = int(request.GET.get('id'))
    context = {
        "id": id
    }
    return render(request, "contact.html", context)


def post_reg(request, id=10, foo='me'):
    # id = int(request.GET.get('id'))
    context = {
        "id": id,
        "foo": foo
    }
    return render(request, "contact.html", context)
