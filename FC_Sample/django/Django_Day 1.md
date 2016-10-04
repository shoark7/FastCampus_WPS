# 파이썬 튜토리얼 정리
<p style='text-align:right'>2016 / 10 / 04 박성환</p>


# Part 1. [Requests and responses](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)

간단한 poll 앱을 만드는 과정을 4파트로 나눠서 진행한다. 나같은 경우 basicpoll이라는 파일을 만든 후 모든 세팅을 마친 후 진행한다.<br><br>


## 1.1.  Setting
pyenv 설정을 마친 후, **프로젝트를 실행할 폴더에서 이동 후** 터미널로 다음과 같이 실행한다.
> django-admin startproject *mysite*

다음과 같이 실행하면 DB, 장고, 어플리케이션 관련 설정을 마친 후 프로젝트가 자동 생성된다.<br>
이때 'django', 'test'와 같이 장고 예약어와 겹칠 수 있는 이름은 사용하지 않는다.

다음과 같은 구조로 프로젝트가 생성된다.
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
* _mysite_ : 프로젝트를 담는 단순한 컨테이너이다. 
* manage.py : 장고 프로젝트와 다양한 방법으로 소통할 수 있게 해주는 커맨드 라인 도구이다. [다음](https://docs.djangoproject.com/en/1.10/ref/django-admin/)에서 관련 파일을 모두 읽을 수 있다.
* mysite : 두 번째 'mysite'가 실제적 프로젝트 폴더이다.
* \__init__.py : 이 파일이 있음으로 해서 파이썬이 이 디렉토리가 파이썬 패키지로 인식된다.
* settings.py : 파이썬 프로젝트의 환경설정과 세팅을 다룬다.
* urls.py : 이 프로젝트의 URL에 관한 선언들이 담겨 있다.
* wsgi.py : 프로젝트를 서빙하기 위한 WSGI-compatible web의 진입점이다.~~모르겠다.~~<br>


## 1.2. 서버 실행
장고 서버가 실행되는지 확인하기 위해서는 다음과 같이 입력한다.
> python manage.py runserver

장고 버전과 함께 'http://127.0.0.1:8000'이 함께 나오면 성공이다. 이 명령어를 통해 장고에서 기본 제공하는 가벼운(lightweight) 서버를 확인했다. 이 서버는 개발상황을 확인할 때만 쓰도록 한다.

> python manage.py runserver 3000

와 같이 포트를 지정하거나, IP 주소도 지정할 수 있다.

> ** runserver의 자동 리로딩 **
> 장고 서버는 코드가 업데이트 될때마다 자동으로 다시 시작한다. 그러나 파일을 더하는 등 어떤 행동들은 재시작이 되지 않기 때문에 직접 시작해주어야 한다.<br>


## 1.3. APP 만들기
프로젝트 설정을 마쳤으니 이제는 APP을 만들도록 하자. 둘은 엄연히 다른데, APP이 무언가를 하는 웹 어플리케이션이라면 프로젝트는 APP은 물론 환경설정까지의 집합을 일컫는다. 그래서 한 프로젝트의 여러 APP이 담길 수 있다.

APP은 어디에도 있을 수 있는데 여기서는 *manage.py* 바로 옆에 두도록 한다. APP을 만드는 명령어는 그래서 디렉토리를 신경 써서 만들도록 한다.

> python manage.py startapp poll

결과 이런 구조의 'poll' 폴더가 만들어 졌을 것이다.
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```


## 1.4. 첫 view 쓰기
 poles라는 APP에는 그 APP에 해당하는 view가 있고 그 안에 코드를 적는다. 그리고 그 뷰가 실행되기 위해서는 그것을 url과 매핑해야 하며 그래서 APP에 urls.py를 만든다.
 
 수업 시간에 배운 것과 달리 APP에 url 정보를 담으면 프로젝트에 있는 루트 url에 정보를 담아줘야 한다. 이때 django.conf.url의 include 메소드를 사용한다.

 
## 1.5. url 함수의 인자
>  url( regex, view )

* 1. regex : 매핑할 url을 찾을 정규표현식이다. 성능상, 정규표현식은 URLconf 모듈이 처음 로드될 때 자동으로 컴파일 된다. 매우 빠르다.
* 2. view : 정규표현식이 매치되면, 장고는 특정한 view 함수를 호출한다.




# Part 2. [데이터베이스 세팅](https://docs.djangoproject.com/en/1.10/intro/tutorial02/)

## 2.1. 기본 세팅
### 2.1.1
먼저 settings.py를 먼저 에디터로 연다. 디폴트로 SQLite를 사용하며 따라서 추가적으로 설치하지 않아도 된다. 그러나 실제 프로젝트에서는 PostgreSQL와 같은 더 강력한 데이터베이스를 사용할 수도 있을 것이다.<br>
데이터베이스를 변경하고 싶다면 settings.py에서 DATABASES 모듈 변수를 수정해주면 된다. 'ENGINE', 'NAME'이 있을 것이고 사용하고자 하는 옵션에 맞게 수정해주어야 한다. **SQLite가 아닌 다른 데이터베이스를 사용한다면 ID, PASSWORD, HOST 등의 정보도 같이 입력해주어야 한다.**
<br>

### 2.1.2.
 INSTALLED_APPS 에 장고에서 사용할 모든 어플리케이션이 등록된다.
 기본으로 들어가 있는 변수들은 다음과 같다.
 
* django.contrib.admin – 관리자 사이트. 잠시 사용한다.
* django.contrib.auth – 인증 시스템
* django.contrib.contenttypes – 컨탠츠 타입을 위한 프레임워크
* django.contrib.sessions – 세션 프레임워크
* django.contrib.messages – 메세징 프레임워크
* django.contrib.staticfiles – static파일을 관리하는 프레임워크

 이 어플리케이션들은 데이터베이스 테이블이 적어도 하나 필요하므로 우리가 맨처음 하나 만들어주어야 한다. 
 > python manage.py migrate
 
 migrate 명령어는  INSTALLED_APPS 세팅을 살펴본 뒤 **필요한 데이터베이스 테이블을 만든다. migrate는 오직 INSTALLED_APPS안의 앱만 관리한다.**
 
## 2.2 모델 만들기
### 2.2.1. 모델의 철학
> 모델이란 데이터에 대한 단일하고 명확한 소스이다. 꼭 필요한 데이터의 필드와 행동을 담고 있다. 장고는 [DRY](https://docs.djangoproject.com/en/1.10/misc/design-philosophies/#dry)원칙을 따르고 있다. 이것은 루비와 달리 migrations를 포함한다.<br>
 
  django.db.models.Model을 상속받는 클래스를 만들면 그게 곧 모델이다. 각 모델은 를래수 변수를 가지며 그것들은 데이터베이스의 필드에 해당한다.<br>
 그리고 각 필드는 Field 클래스의 인스턴스를 자료형으로 갖는다.<br>
 어떤  Field classes는 인자를 필요로 하는데 예를 들어, CharField 같은 경우 max_length가 주어져야 한다. 데이터베이스 스키마에서 뿐 아니라 validation에서도 곧 보게 될 것이다.
 
## 2.3. 모델 실행하기
프로젝트에 앱을 포함하기 위해서는 INSTALLED_APPS에 셋팅을 해주어야 한다. apps.py 파일에 설정 클래스가 들어 있으며 그 파일 경로를 INSTALLED_APPS에 넣어줘야 한다.
 
 
```python

INSTALLED_APPS = [
    'polls.apps.PollsConfig', ## 여기
    'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
]
```

> python manage.py makemigrations polls

다음 명령을 넣어줌으로써 장고에 모델에 변화가 생겼으며 이 변화를 _migration_에 저장하라고 말하게 된다.

> python manage.py migrate 

다음 migrate 함으로써 그 모델을 생성하게 된다.  일종의 커밋 후 푸쉬하는 느낌이다. migrate는 적용되지 않는  migrations들을 모두 추적해서 적용한다.

> python manage.py sqlmigrate poll 0001

다음과 같이 입력해서 우리가 입력한 클래스가 어떻게 SQL로 해석되는지 확인해볼 수도 있다. 이것이 곧 ORM!!

> 즉 모델에 변화를 주는 세 가지 방향은
> 1. models.py를 수정한다.
> 2. `python manage.py makemigrations` 로 그 변화들에 대한 마이그레이션을 만든다.
> 3. `python manage.py migrate`로 변화를 적용한다.



## 2 .4. API가지고 놀기
 free API Django를 가지고 놀아보자. 다음을 입력.
 
 > python manage.py shell
 
 일반과 같은 파이썬 쉘이 나타난다. 일반 쉘과 달리 manage.py가 ' DJANGO_SETTINGS_MODULE' 환경변수를 집어넣고 그 변수는 장고에게 settings.py 파일을 임포트할 수 있는 경로를 주게 된다.
 그리고 다음과 같이 입력한다.
 
 > from polls.models import Question, Choice 
 > Question.objects.all()
 
 위 문장을 통해 모델에 있는 Question, Choice 모델에 접근했고 아래 문장을 통해 Question의 모든 자료를 뽑아올 수 있다.
 
 > q = Question(question_text="What's new?", pub_date=timezone.now())
 > q.save()

위처럼 Question 객체 즉, 데이터 리코드 하나를 만들 수 있고, save를 명시적으로 적어주면 데이터베이스에 등록된다. 데이터 수정 등에도 마찬가지이다.
 
 
## 2.5. Introducing the Django Admin¶
### 2.5.1. 철학
admin 사이트를 만드는 것은 꽤나 지루한 일이다. 따라서 장고는 admin 인터페이스 만드는 것을 완전 자동화하고 있다. 파이썬은 "컨탠츠 퍼블리셔"와 "퍼블릭" 사이트를 구분하고 있다. 장고는 "컨탠츠 퍼블리셔"들을 위한 인터페이스를 기본으로 제공하는 것이다. 즉, 관리자들을 위해 제공된다.

### 2.5.2. 관리자 유저 만들기

> python manage.py createsuperuser

를 입력하면 슈퍼유저의 아이디, 이메일, 비밀번호를 입력하게 되고 입력하면 관리자가 생성되었다.<br>
그러면 바로 관리자 사이트를 경험해볼 수 있다. 서버를 실행한 뒤 url 뒤에 'admin'를 입력하면 관리자 화면이 나온다.

처음 들어가면 'groups', 'users' 의 옵션이 보이는데 이것은 장고의 `django.contrib.auth` 프레임워크에서 제공되는 것이다.

우리의 앱이 관리자 파일에서 추가되게 하려면 'admin.py' 파일에 설정을 해준다.

> admin.site.register(Question)

결과 어드밍 페이지에서 우리의 앱이 추가된 것을 볼 수 있다.


# Part 3. [View]( https://docs.djangoproject.com/en/1.10/intro/tutorial03/)

## 3.1. 개요
'view'란 장고 어플리케이션에 있는 웹페지의 한 타입으로서 특정 기능을 수정하고 본인의 템플릿이 있는 것을 말한다. <br>
만약 블로그라면, 블로그 홈페이지, 커맨트, 인덱스 페이지, 결과 페이지 등의 뷰가 있어야 할 것이다.<br>
장고에서는 웹페이지는 뷰를 통해 전달이 되고, 각각의 뷰는 간단한 파이썬 함수나 CBV의 인스턴스로 표현된다. 장고는 URL을 검사한 뒤, 뷰를 선택할 것이다. 
<br>
장고는 복잡한  URL대신 _elegant URL  patterns_, 우아한 URL을 지원해서 간단하게 url을 만든다.
URL이 뷰로 가기 위해서는 장고는 ‘URLconfs’라는 것을 사용한다. URLconf는 정규표현식으로 표현되는 URL patterns을 매핑해서 뷰로 넘긴다.
<br>
이번 예제는 URLconfs에 대한 기본 소개이다.

## 3.2. 뷰 더 작성하기
튜토리얼과 같이 뷰를 더 작성한다. 잊지 말자 언제나 뷰는 url과 연결되어 있고 따라서 뷰를 작성하면 url과 이어줘야 한다. 정규표현식으로 어떻게 url이 매칭되는지 다음과 같이 보자.
```python

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```
저기서 기억할 건 매칭은 끊어서 순서대로 넘어간다. 	`polls/34/results`경로를 찾았다면 첫 번째 조건에서 'polls'가 충족에서 나머지가 다음으로 넘어간다. '34'도 만족되며 'results'가 만족된다. 

<br>