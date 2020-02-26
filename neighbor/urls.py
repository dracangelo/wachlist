from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='homepage'),
    url(r'^update_profile/$', views.add_profile, name='update_profile'),
    url(r'^profile/$', views.profile, name='profile'),

]



