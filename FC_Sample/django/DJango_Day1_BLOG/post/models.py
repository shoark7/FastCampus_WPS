from django.db import models


# 이 클래스는 곧 데이터베이스의 테이블이다.
# 그리고 '*Field' 클래스의 인스턴스를 받는 클래스 변수는 곧 테이블의 열이 된다.

class Post(models.Model):                               # 데이터 베이스에서 테이블이 된다.
    # 제목
    title = models.CharField(max_length=30)             # max_length라는 인자를 통해 글자가 제한된다.
    # 간단 설명
    description = models.CharField(max_length=100)
    # 본문내용
    content = models.TextField()                        # 긴 글을 받는다.
    # 생성일자
    created = models.DateTimeField(auto_now_add=True)   # 시간 자동 생성
    # 좋아유 수
    like_count = models.IntegerField(default=0)         # default로 기본값 설정이 가능하다.

    view_count = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    # 이 함수가 정의되어야 쉘 등에서 각 레코드가 가독성 있게 표현된다.
