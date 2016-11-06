# DJango day 9.
### 2016/10/18. 화요일
### 박성환

### 오늘 진도 내용
유투브 API를 통해 동영상 정보를 가져오고, 나만의 유투브 북마크 앱 꾸미기

### 오늘 정리할 내용.
> 1. 장고 `request`의 `path`, `get_full_path`, 그 차이를 묻다.
> 2. `pip list`와 `pip freeze`의 차이
> 3. `django.contrib.humanize`란?
> 4. 파이썬에서 `__all__`란?



<Br><BR>

## 1. get_full_path, path. 그 차이를 묻다.
장고 5~7일 차에 회원가입, 로그인 기능을 구현하면서, 로그인 후 유저를 유저가 로그인(가입) 전 있던 페이지로 `redirect`하는 방법에 대해 되었다.<br>
한영 샘이 제시해주신 방법은 현재 _url_을 값으로 하는, `next`라는 임의의 키를 템플릿에서 GET 방식으로 보내서 로그인 후 그 값을 불러들여 유저를 해당 페이지로 보내는 방식이다.

```django
<ul class="nav navbar-nav navbar-right">
          {% if user.is_authenticated %}
          	... 이하 생략 ...
            <a href="{% url 'member:login' %}?next={{ request.path }}">Login</a>
          </li>
          <li>
            <a href="{% url 'member:signup3' %}?next={{ request.path }}">Signup</a>
	    	... 이하 생략 ...
             	
            <a href="{% url 'video:search' %}">검색하기</a>
	  </li>
</ul>
```
_url reversing_으로 urlConf에 `member`앱의 `login` 네임을 가진 url을 보내게 될 것이라는 것은 모두가 알 것이다.<br><BR>

여기서 유의할 것은 바로 `?next={{ request.path }}`. `?` 뒤에 오는 것은 쿼리 스트링에서 그 유명한 GET 메서드에서 쿼리스트링을 보내는 방식이다. `next` 키에 `request.path`, 즉 현재 페이지의 경로값을 보내는 것이다. <br>
이 값을 통해 로그인 처리를 한 후, 로그인이 성공하면 `next`키 값의 `value`로 `redirect`하면 사용자가 있던 자리로 돌아올 수 있을 것이다.<br><BR>

그러면 이제 질문해야 한다. `request.path`는 뭐지?

### HttpRequest.path
> 문서에 따르면 `path`값은 요청된 페이지까지의 전체 경로의 문자열을 의미하는데, 스키마(http 등)나 도메인(www.naver.com 등)은 포함하지 않는 값이다.
<br>
> 예를 들면,  "/music/bands/the_beatles/"와 같은 값이 있을 것이다. 그리고 마찬가지로 유용하고 비슷한 기능이 있다.

<br>

### HttpRequest.get_full_path()
> `path`와 마찬가지로 경로를 반환하는데, **query string**까지도 가능하면 같이 반환한다.
> 예를 들면 "/music/bands/the_beatles/?print=true"와 같이 들 수 있을 것이다.
<br>

둘의 차이는 먼저 `HttpRequest.path`는 쿼리스트링을 적용하지 않는다. 그러니까, 쿼리스트링을 붙여 GET 메소드로 전송한 url일지라도 `path`는 쿼리스트링을 빼고 전달한다. 단순히 리스트 등을 출력하는 view에 사용하면 유용할 것이다.<br><BR>

반대로, `HttpRequest.get_full_path()`는 쿼리스트링을 포함하는 경로까지 포함한다. 만약 사용자가 포스트의 구체적인 목록에 들어와서 글을 읽고 있었다면, 쿼리스트링을 포함하는 이 방법이 나을 것이다. 이 둘은 상황에 맞게 사용하면 될 것 같다.<br><BR>

또한, `HttpRequest.path`는 속성인 반면, `HttpRequest.get_full_path()`는 메서드라는 차이가 또 있다.

<br><br><br>
## 2. 'pip list', 'pip freeze'
나를 포함해서 많은 사람들이 _virtualenv_에 설치된 라이브러리의 종류와 그 버전을 확인할 때 커맨드 창에서 `pip list`를 많이 사용해봤을 것이다. 명령어를 사용하면 다음과 같이 설치된 라이브러리와 그 버전이 나온다.

```
user@user-VirtualBox:~$ pip list
feedparser (5.1.3)
pip (1.4.1)
setuptools (1.1.5)
wsgiref (0.1.2)
user@user-VirtualBox:~$ pip freeze
feedparser==5.1.3
wsgiref==0.1.2
```
음. 이것만으로도 사실 훌륭하다. 그런데 좋은 활용성을 지닌 비슷한 다른 기능도 존재한다. 바로 `pip freeze`이다.<br><BR>

`pip freeze`도 현재 환경에서 설치된 라이브러리와 그 버전이 표현된다. 그런데 그 표현방식이 조금 다르다. 바로 확인해본다.

```
user@user-VirtualBox:~$ pip freeze
feedparser==5.1.3
wsgiref==0.1.2
django==1.4.2
```
뭐가 다른 것일까? 문서에서는 다음과 같이 표현한다.<br><BR>

`pip freeze` : Output installed packages in **requirements format.**
<br>

생각해보자. 내가 어떤 파이썬 프로젝트에 참여했다. 프로젝트에서 모든 팀원이 같은 환경을 공유하는 것이 중요할 것이다. django는 어떤 버전, six는 어떤 버전 등등. 버전 차이간 오류를 원하지 않으면 미리 버전을 맞추는 것이 상책이다.<br><BR>

그런데 지금 참여한 내가 어떤 버전을 설치할지 어떻게 알까? 일일히 선배가 라이브러리와 버전을 설명한다? 엄청난 시간낭비일 것이다.

이때 `pip freeze`를 사용한다. 터미널에서 다음과 같이 입력한다.
```
>>> pip freeze > requirements.txt
```
`pip freeze`의 결과를 requirements.txt에 저장한다. 아까 보았던 _required format_이다. 
```
pip install -r requirements.txt
```
이렇게 입력하면 requirements.txt의 내용들을 recursive(-r)하게 읽어들이면서 모든 설정을 다 설치할 것이다. 이 방법을 통해 프로젝트 팀원간 버전 통일을 이루어낼 수 있다.

<br><BR>
이런 특수한 목적을 가졌다면 `pip freeze`를 사용하는 것이 좋을 것이다.


<br><br><br>
## 3. django.contrib.humanize란?
문서에 의하면 장고는 파이썬의 '[batteries included](https://docs.python.org/3/tutorial/stdlib.html#tut-batteries-included)'철학을 따르는 것을 목표로 하고 있다고 한다. 장고는 웹개발과 관련한 다양한 추가적인 도구들을 지원한다.<br><BR>

장고의 이 코드는 `django.contrib` 패키지에 모아져 있다. 우리에게 익숙한 `django.contrib.auth`도 인증과 관련한 다양한 도구들을 지원하는 것과 마찬가지다.

<bR><BR>

`django.contrib.humanize`는 **데이터에 '사람의 손길'을 더할 수 있다는 템플릿 태그들의 집합이다.** 이 필터들을 활성화하기 위해서는 `django.contrib.humanize`를 INSTALLED_APPS에 더해야 한다.<br> 그 후 `{% load humanize %}` 태그를 템플릿 안에 로드해주면 사용할 수 있다. 유용한 몇 개 기능만 살펴보도록 한다.

### 3.1. intcomma
아라비아 숫자에 1000의 자리마다 ' ,' 를 붙여준다. 괄호 안의 값은 해당 변수가 같는 값이라는 의미로 설명의 편의를 위해서 넣었다.
`{% value(4500)|intcomma %}` ---> 4,500

### 3.2. ordinal
단어 그대로 서수를 영어로 표현할 수 있다.
`{% value(1)|ordinal %}` ---> 1st.
`{% value(2)|ordinal %}` ---> 2nd

### 3.3 naturalday
오늘과 오늘을 기준으로 하루 이내의 날짜를 'today', 'yesterday', 'tomorrow'로 표현한다. 인자로 `date ` tag에 들어온 값을 받는다.<br><BR>

오늘이 '17 Feb 2016'이라면,<br>
`{% value(16 Feb 2016)|naturalday %}` ---> yesterday
`{% value(17 Feb 2016)|naturalday %}` ---> today
`{% value(18 Feb 2016)|naturalday %}` ---> tomorrow


<br><br><br>
## 4. 파이썬에서 __all__ 은 무엇일까?
파이썬에서 \__add__,\ __ge__ 등은 본 적이 있다. 그런데 \__all__은 오늘 처음 봤는데 디렉토리간 관계가 깊은 큰 프로젝트에서 유용하게 사용할 수 있을 것 같다. 바로 살펴본다.

```
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
```
본 예시는 밑의 출처의 jump to python의 예제를 그대로 가져왔음을 밝힌다. 좋은 자료에 감사한다.<br><BR>

위 관계도를 보자.<br>
game이라는 큰 패키지 안에 sound, graphic, play라는 패키지가 있고, 각 패키지는 또 자신의 모듈을 가지고 있다. 알다시피, 파이썬 인터프리터는 **디렉토리 안에 `\__init__.py`가 들어가 있으면 그 디렉토리를 파이썬 패키지로 인식한다.**<br><BR>

파이썬을 모듈을 쓰면서  `from string import *`와 같이 쓸 수도 있다는 것을 알고 있을 것이다.  string 모듈의 모든 함수, 속성을 쓰겠다는 의미이다.<br> 일반적으로는 이렇게 쓰지 말라고 한다. namespace가 섞일 수 있기 때문이다.  \__all__는 이것과 관련이 있다.<br><BR> 

```python
/Python/game/sound/__init__.py
__all__ = ['echo']
```
아까 본 sound는 패키지이다. 이 패키지는 echo와, wav라는 모듈을 가지고 있다. 만약,<br>
`from game.sound import *`라고 입력한다면 두 모듈이 모두 임포트되어야 하지만 \__ini__.py 안에 **\__all__ = ['echo']**와 같이 적으면 echo 모듈만 임포트한다. 대규모 프로젝트에서 한 패키지의 모든 모듈을 임포트하지만, 이름이 겹치는 특정 모듈만 빼고 싶을 때  위 방법을 쓰면 유용할 것이다.<br><BR>

그러나 `from game.sound.echo import *`와 같이 쓰면 echo 안의 모든 것을 import한다. 애초에 echo는 패키지가 아니라 모듈이며, 모듈에 \__init__.py가 적용되지 않는다. \__init__.py는 패키지 단위 모듈이라는 것을 잊지 말자.


<br><br>
#### 출처 :
1. get_full_path, path. 그 차이를 묻다.
	- [Django httprequest document](https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpRequest.read)
	
2. 'pip list' vs 'pip freeze'
	- [pip list vs pip freeze - stackover-flow](http://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list)
	
3. django.contrib.humanize란?
	- [humanize django doc](https://docs.djangoproject.com/en/1.10/ref/contrib/humanize/)
	- [contrib django doc](https://docs.djangoproject.com/es/1.10/ref/contrib/)
	
	
4. 파이썬에서 __all__ 은 무엇일까?
	- [점프 투 파이썬 - 패키지](https://wikidocs.net/1418)
