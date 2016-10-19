from django.contrib import admin
from .models import Post # 현재 위치 models 파일에서 Post 객체 임포

# 장고 어드민 사이트에 Post 모델을 등록한다.
# 그러면 사이트에서 Post앱을 관리할 수 있다.
admin.site.register(Post)