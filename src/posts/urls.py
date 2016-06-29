from django.conf.urls import include, url
# from . import views
from .views import (
    post_list,
    post_create,
    post_detail,
    post_delete,
    post_update,
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'posts.views.post_home', name='home_id'),
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^(?P<id>\d+)/$', post_detail, name='post_detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name='post_delete'),

    # url(r'^(?P<id>\d+)/$', 'posts.views.post_reg', {'foo': "bar"}, name='home_id'),

    # url(r'^(?P<id>\d+)/$', views.post_id, name='home_id'),
    # url(r'^$','posts.views.post_home', name='home'),

]
