11.  Request & Response
12.  Mapping URL so to Views
13.  In App  URLs
14.  Django Templates
15.  Template Context
16.  QuerySet Basics
      - python  manage.py shell
        from  posts.models  import  Post
        Post.objects.all() <return _str_>
        Post.objects.filter(id=3)
        Post.objects.filter(title__icontains="post")

        query =  Post.objects.all()
        for obj in query:
            print  obj.id
            print  obj.title
            print  obj.timestamp

        Post.objects.create(title="mypage", content="hello")


17.  Get Item or 404 Query
     - instance = get_object_or_404(Post, title="New Post")
       instance = Post.objects.all()

18.  Dynamic Url Routing & Patterns

      -urls.py
       url(r'^detail/(?P<id>\d+)/$', post_detail, name='post_detail'),

      -views.py
      post_detail(request,id=None)
        instance = get_object_or_404(Post, id=id)

19. URL Links  & Get Absolute URL
    index.html
     1.   <a href='/posts/{{ obj.id }}/'> {{ obj.title }} </a> <br/>
     2.
       - urls.py
           url(r'^(?P<id>\d+)/$', post_detail, name='post_detail'),
       - index.html
           <a href='{% url "post_detail" id=obj.id %} '> {{ obj.title }} </a> <br/>

      3.
        - models.py
          from django.core.urlresolvers import reverse

          def get_absolute_url(self):
              return reverse("post_detail",kwargs={"id": self.id})
              #return "/posts/%s/" %(self.id)

        - index.html
           <a href='{{ obj.get_absolute_url }}' > {{ obj.title }} </a>

      4
        - urls.py on trydjang19
          url(r'^posts/', include('posts.urls', namespace='posts')),

        - models.py
         def get_absolute_url(self):
         return reverse("posts:post_detail",kwargs={"id": self.id})

20. Model From & Create View
       - forms.py
         from django import forms
         from .models import Post

         class PostForm(forms.ModelForm):
            class Meta:
                Model = Post
                fields = [
                    "title",
                    "content"
                ]

       - view.py
          def post_create(request):
            form = PostForm(request.POST or none)
            if form.is_valid():
               instance = form.save(commit=False)
               instance.save()
             context = {
                 "form":  form
             }

             return render(request, "post_form.html", context)

       - post_form.html

       <form method="POST" action="">
           {% csrf_token %}
           {{  form.as_p }}
           <input type="submit">
       </form>

21. Instance Update View.

import django  from  HttpResponseRedirect

- views.py

    def post_update(request,id=None):
        instance  = get_object_or_404(Post,  id=id)
        form  = PostForm(request.Post or None, instance=instance)
        if form.in_valid():
            instance  = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "title": instance.title,
             "instance": instance,
             "from": from,
             }
         return  render(request, "post_form.html", context)

- url.py
       url(r'^(?P<id>)\d+)/edit/$', post_update, name='update'),

22. Django Messages Framework

- views.py
    import django.contrib  import messages

    def post_create(request):
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
*           messages.success(request, "Successfully Created")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
*           message.error(request, "Not Successfully Created")

         context = {
            "form": form,
          }
         return  render(request, "post_form.html", context)

    def post_update(request, id=None):
        form  = PostForm(request.POST or None, instance=instance )
        if form.is_valid():
            instance = form(commit=False)
            instance.save()
*           messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
            return HttpResponseRedirect(instance.get_absolute_url())
        context =  {
            "title": instance.tilte,
            "instance": instance,
            "form": form,
        }
        return  render(request, "post_form.html", context)

- post_detail.html

{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li {% if message.tags %}
        class="{{ message.tags }}"
        {% endif %} >
            {% if "html_safe" in message.tags %}
              {{ message|safe }}
            {% else %}
              {{ message }}
            {% endif %}
    </li>
    {% endfor %}


23. Delete View.

import  from django.shortcuts import redirect
- views.py
    def post_delete(request,id=None):
        instance = get_object_or_404(Post, id=id)
        instance.delete()
        messages.success(request. ""
        return redirect("posts:list")

- urls.py
    url(r'^$', post_list, name='list'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),


24.  Templates  & Inheritance

    {% extended  base.html  %}  Call master class.

     - base.html
     [  {%block content %}{% endblock content %}  ]

     - post_list.html
      {% extends "base.html" %}
      {% block content %}
      // do something
      {% endblock content %}

      - views.py
      def post_list(request):
          print settings.BASE_DIR
          queryset = Post.objects.all()

          context = {
            "title": "List",
             "object_list":  queryset,
          }
          return render(request, "post_list.html", context)

      // show base.html but rewrite block content //

25.  Setup Static  Files - CSS & Javasc

# (python): python  manage.py  collectstatic

 * when create base.css on  /src/static and run command  python  manage.py collectstatic directory and file copy to   /static_cdn

-- settings.py

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),

    ]

    #system  static file
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

-- urls.py

    from django.conf.urls.static import static
    from django.conf import settings

    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

-- base.html
     {% include "messages_display.html" %}
     <link rel="stylesheet" href= '{% static  "css/base.css" %}' />
     <img src ='{% static "img/beach.jgp" %}'>

-- /src/static/css/base.css
    h1 {
        color: #00db6e;
    }

26. implement bootstrap.
        http://getbootstrap.com/getting-started/

--base.html
        <head>
             <!-- bootstrap -->
            <link href='{% static "css/bootstrap.min.css" %}' rel="stylesheet">
            <link href='{% static "css/bootstrap-theme.min.css" %}' rel="stylesheet">

        </head>
        <body>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src='{% static "css/bootstrap.min.js" %}'></script>

--detail.html
        <div class="col-sm-6 col-sm-offset-3">
        <h1> {{ title }}  <small> {{ instance.timestamp }} </small> </h1>

--list.html
        <div class='col-sm-8 col-sm-offset-3'>

    {% for obj in object_list %}
    <
    <div class="row">
        <div class="col-sm-12">
            <div class="thumbnail">
                <div class="caption">
                    <h3><a href='{{ obj.get_absolute_url }}'> {{ obj.title }} </a>
                        <small> {{ obj.timestamp| timesince}} ago</small>
                    </h3>
                    <p> {{ obj.content | linebreaks | truncatechars:120 }} </p>
                    <p><a href='{{ obj.get_absolute_url }}' class="btn btn-primary" role="button">View</a></p>
                </div>
            </div>
        </div>
        <hr/>
    </div>
    {% endfor %}

--form.html
    <div class='col-sm-6 col-sm-offset-3'>

27. Pagination by Queryset
-- views.py
    Post.object.all() #.order_by("-timestamp")

-- models.py
    class Post(models.Model):
    ...
      class Meta:
         ordering = ["-timestamp", "-updated"]

--views.py

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
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
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, 'post_list.html', context)