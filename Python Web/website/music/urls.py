from django.conf.urls import  include,url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    #detials for any album with id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #all artist
    url(r'^artist/$',views.artist,name="artist"),
]
