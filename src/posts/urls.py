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
    url(r'^$', post_list, name='post_list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^detail/$', post_detail, name='post_detail'),
    url(r'^update/$', post_update, name='post_update'),
    url(r'^delete/$', post_delete, name='post_delete'),

    url(r'^(?P<id>\d+)/$', 'posts.views.post_reg', {'foo': "bar"}, name='home_id'),

    # url(r'^(?P<id>\d+)/$', views.post_id, name='home_id'),
    # url(r'^$','posts.views.post_home', name='home'),

]
