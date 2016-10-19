"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from blog import views as blog_views
from mysite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # blog/urls.py를 사용하지 않고 루트 urls.py를 사용할 경우
    # url(r'^$', blog_views.post_list, name='post_list'),

    # blog/urls.py의 내용을 사용할 경우
    url(r'', include('blog.urls', namespace='blog')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^video/', include('video.urls', namespace='video')),

    # Common
    url(r'^error/$', views.error, name='error'),
    url(r'^test/(?P<pk1>[0-9]+)/(?P<pk2>[0-9]+)/$', views.test, name='test'),
]
