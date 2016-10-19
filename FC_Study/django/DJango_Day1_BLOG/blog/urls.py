"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/httppost_list/urls/
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
from django.conf.urls import url
from django.contrib import admin
from post.views import post_list # post_list를 import해야 이 뷰를 사용할 수 있다.



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/list/', post_list), # url을 넣어줌으로써 '기본경로/post/list' 입력시 post_list가 실행되게 되었다.
]                                   # 만약 'urls.py'를 앱 내에 자체적으로 넣었다면 여기서 include를 써주어야 했을 것이다.
