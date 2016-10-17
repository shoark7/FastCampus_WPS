from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^add_star/$', views.add_star, name='add_star'),
    url(r'^star_list/$', views.star_list, name='star_list'),
    url(r'^detail/(?P<pk>\d+)/$', views.star_detail, name='star_detail'),
    url(r'^star/delete/(?P<pk>\d+)$', views.star_delete, name='star_delete'),
]