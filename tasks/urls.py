from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/', views.index, name='index'),
    url(r'^up', views.say_whatsup, name='whatsup'),
    url(r'^down', views.swag, name='swag'),
    url(r'^create', views.create, name='create'),
    url(r'^delete/(?P<task_id>[0-9]+)', views.delete, name='delete'),
    url(r'^toggle/(?P<task_id>[0-9]+)', views.toggle, name='toggle')

]

