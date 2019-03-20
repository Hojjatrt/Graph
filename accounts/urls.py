from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.update_profile, name='profile'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
]
