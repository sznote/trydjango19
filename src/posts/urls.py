from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    #url(r'^$', 'posts.views.post_home', name='home_id'),
    url(r'^$', 'posts.views.post_list', name='post_list'),
    url(r'^create/$', 'posts.views.post_create', name='post_create'),
    url(r'^detail/$', 'posts.views.post_detail', name='post_detail'),
    url(r'^update/$', 'posts.views.post_update', name='post_update'),
    url(r'^delete/$', 'posts.views.post_delete', name='post_delete'),

    url(r'^(?P<id>\d+)/$', 'posts.views.post_reg', {'foo': "bar"}, name='home_id'),

    # url(r'^(?P<id>\d+)/$', views.post_id, name='home_id'),
    # url(r'^$','posts.views.post_home', name='home'),

]