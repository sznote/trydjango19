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