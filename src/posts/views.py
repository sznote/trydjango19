from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Post


#  Shell python manage.py Shell
# from posts.models import Post
#  Post.objects.all()

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>created</h1>")


def post_detail(request):
    #instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=3)

    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    print settings.BASE_DIR

    queryset = Post.objects.all()

    context = {
        "title": "List",
        "object_list":  queryset,
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title":  "My User List"
    #     }
    # else:
    #     context ={
    #         'name': "sahai",
    #         'tel': "0809700084",
    #         "title": "List",
    #     }
    return render(request, "index.html", context)


def post_update(request):
    context = {
        "title": "Update"
    }
    return render(request, "index.html", context)


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
