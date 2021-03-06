from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Post
from .forms import PostForm


#  Shell python manage.py Shell
# from posts.models import Post
#  Post.objects.all()

# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #print form.cleaned_data.get("title")
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.success(request, "Not Successfully Created")

    #if request.method == "POST":
        #print request.POST
        #print request.POST['content']
        #print request.POST.get('content')

    context  = {
        "form": form,
    }

    return render(request, "post_form.html", context)


def post_detail(request,slug=None):
    #instance = Post.objects.get(id=1)
    #instance = get_object_or_404(Post, id=id)
    instance = get_object_or_404(Post, slug=slug)

    context = {
        "title": "Detail",
        "instance": instance,
        "id": id
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    print settings.BASE_DIR

    # queryset = Post.objects.all() #.order_by("-timestamp")
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "List",
        "object_list": queryset,
        "page_request_var": page_request_var
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
    return render(request, "post_list.html", context)

def post_update(request, id=None):

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,  instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)   #save method posts form to instance
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
        "id": id,
    }

    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()

    messages.success(request,"Successfully Deleted")
    return redirect("posts:list")


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
