from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register', views.register, name='index'),
    url(r'^login', views.login, name='index'),
    url(r'^logout', views.logout, name='logout')

]
