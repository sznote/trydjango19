from django.conf.urls import include, url
from . import views

urlpatterns = [
    #Examples:
    url(r'^(?P<id>\d+)/$','posts.views.post_id', name='home_id'),
    url(r'^$','posts.views.post_id', name='home_id'),
    #url(r'^(?P<id>\d+)/$', views.post_id, name='home_id'),
    #url(r'^$','posts.views.post_home', name='home'),

]