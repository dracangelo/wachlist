from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^$', views.homepage, name='homepage'),
    url(r'^add_hood/$', views.add_hood, name='add_hood'),
    url(r'^join_hood/(\d+)', views.join_hood, name='join_hood'),
    url(r'^leave_hood/(\d+)', views.leave_hood, name='leave_hood'),
    url(r'^add_biz/$', views.add_biz, name='add_biz'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^user/(?P<username>\w+)', views.user_profile, name='user_profile'),
    url(r'^new_profile/$', views.add_profile, name='add_profile'),

]

