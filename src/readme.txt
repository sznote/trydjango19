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

18.