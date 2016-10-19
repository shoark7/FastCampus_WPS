from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from member.models import MyUser


def signup(request):
    """
    회원가입을 만들어주세요
    가입후에 message에 info tag로 '%s님 %s아이디로 회원가입 되었습니다'

    0. base.html에 signup링크 연결되는 a태그 구현 (로그인 안 되어있을 때만)
    1. views.py에 위 함수 추가 (빈 내용)
    2. urls.py에 연결 (signup/)
    3. 사용할 템플릿 구성 (form)
    4. form요소에 회원가입에 필요한 필드 구현 (email, password, nickname, last_name, first_name)
    5. views.py에서 POST요청을 받아 확인
    6. views.py에서 받은 값들을 사용해 MyUser모델 생성
    7. 생성 완료 후 해당 User로 로그인
    8. message.info(request, '메세지내용')으로 request에 메세지 전달
    9. 모든 과정 완료 후 'blog:post_list'로 redirect

    # Extra
    - Signup으로 오기 이전 URL로 redirect
    - login을 통해서 signup으로 온 경우에도 login이전에 있던 페이지로 redirect
    - MyUserManager의 create_user메서드를 사용
    - ModelForm을 사용, 또는 Form을 사용
    - form에 Bootstrap 클래스를 적용 (form-group, form-control)
    """

    if request.method == 'POST':
        # 키 값 존재하는지 검사
        try:
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']
            nickname = request.POST['nickname']
        except KeyError:
            return HttpResponse('Form필드에 없는 키 값이 있습니다')

        # 패스워드 일치 검사
        if password1 != password2:
            return HttpResponse('패스워드가 일치하지 않습니다')

        # CustomUserManager를 통해 유저 생성
        user = MyUser.objects.create_user(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            password=password1
        )

        # 생성한 유저 로그인
        auth_login(request, user)
        return redirect('blog:post_list')
    else:
        # member/signup.html 파일을 render
        return render(request, 'member/signup.html')


