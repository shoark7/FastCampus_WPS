from django.shortcuts import render, render_to_response
from .models import Post


# post_list라는 이름의 뷰.
# Post 인스턴스를 전부 가져와 posts라는 이름으로 'post_list.html' 템플릿에 전달한다.
def post_list(requests):
    # ORM을 이용해 Post 인스턴스를 전부 가져옵니다.
    # 이떄 objects는 테이블의 기본 데이터 매니저.
    # all 함수를 통해 테이블의 모든 데이터를 가져온다.
    posts = Post.objects.all()

    # 템플릿에 전달할 딕셔너리 객체
    ret = {
        # key값에 posts지정.
        'title': '블로그 글 목록',
        'posts': posts,
    }
    return render_to_response('post_li1st.html', ret)
    # 'render_to_response'는 HttpResponse와 어떤 템플릿을 반환할지를 한 번에 처리하는 함수이다.

