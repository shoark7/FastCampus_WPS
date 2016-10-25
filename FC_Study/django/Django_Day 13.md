# Django Day 13
#### 2016/10/25
#### 박성환

# 1. private configuration file 관리하기
우리는 [my-blog 프로젝트](https://github.com/shoark7/WPS_mysite_project)를 진행하면서 그 프로젝트를 깃허브에서 관리하고 있다. 깃허브는 기본적으로 모두에게 공유되는 시스템이다. 그리고 그것을 우리도 바라고 있다.<br><BR>

그러나 **모두 공개되면 안 되는 파일**이 있지 않을까? 예를 들어 우리 앱의 `mail` api에서는 구글 g메일 계정과 비밀번호를 통해서 메일을 보내는 기능이 있고, 그래서 아이디와 비밀번호가 고스란히 노출되고 있다. 이럴 때 어떻게 해야 할까?<br><BR>

정답은 비밀번호와 같은 **민감한 정보만 담는 파일을 따로 두고, 그 파일을 `.gitignore`에서 관리하는 것**이다. 그렇게 하면 그 파일 자체가 깃허브로 올라가지가 않아서 우리는 안전하게 정보를 관리할 수 있고, 다른 유저들은 우리의 프로젝트를 관람할 수 있다.<br><BR>

원래 `settings.py`에서 관리하던 이메일 관련 설정들은 다음과 같았다.
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '537'
EMAIL_HOST_USER = 'fastcamp*****@gmail.com'
EMAIL_HOST_PASSWORD = '****************'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
믿기 힘들겠지만 실제로 아이디와 비밀번호가 그대로 적혀 있고, 깃허브를 통해서 만천하에 공개되었다. 우리는 저것을 바로잡고자 한다.<br><BR>

1. 프로젝트 폴더 내에 `.conf`라는 폴더를 만든다. 이름은 자신에게 맞는 이름을 지으면 된다.
2. 이번 경우에 우리는 json 파일 형태로 정보들을 보관했다. `settings_debug.json`파일을 만든다.
3. json 형태로 필요한 정보들을 구조화해서 넣는다. 파이썬에서 딕셔너리 쓰던대로 쓰면 문제가 발생하는데, json은 다음과 같은 형식을 지켜야 한다.
	- 작은 따옴표(')를 쓰지 않는다. 파이썬과 달리 문자열을 감쌀 때는 큰 따옴표만 사용해야 한다.(")
	- 구조의 끝에 ','를 넣지 않는다. 파이썬의 경우에는 스타일가이드에서 제안하고 있을 정도로 보편화된 방법이지만 json 형식은 이를 지원하지 않는다.
	- true, false에는 대문자가 들어가지 않는다. 자바스크립트 자체의 문법으로, json은 자바스크립트 형식이므로 이를 지켜줘야 한다.
<br><br>

만든 json 파일은 대략 다음과 같을 것이다.
```json
{
  "email": {
    "EMAIL_HOST": "smtp.gmail.com",
    "EMAIL_PORT": "587",

    "EMAIL_HOST_USER": "*******@gmail.com",

    "EMAIL_HOST_PASSWORD": "****************",
    "EMAIL_USE_TLS": true
  },
  "facebook": {
    "FACEBOOK_APP_ID": "*******************",
    "FACEBOOK_SECRET_CODE": "*************************"
  }
}
```
'*'가 들어간 건 물론 개인 정보를 가리기 위함이며, 쓸 때는 자신의 진짜 정보를 담아야 한다.<br><BR>

그리고 `.gitignore` 파일 안에 우리의 `settings_debug.json`을 추적하지 않도록 넣어줘야 한다.
```shell
echo '*/conf/' >> .gitignore
```
먼저 우리의 `settings_debug.json`은 `conf` 폴더 안에 있다. **폴더이기 때문에 끝에 '/'를 넣어줘야 한다.** <BR>
'>>' 를 사용함으로써 기존의 `.gitignore`에 덧붙인다.(append) '>'를 하나만 쓰면 지우고 다시 쓰는 것(write)이 되니 조심한다.<br><BR>

이렇게 하면 **`conf` 파일이 추적되지 않으니 그 안에 있는 `settings_debug.json` 또한 자연스럽게 추적을 피하게 된다.** 이제 이 데이터를 아까처럼 그대로 쓰는 것이 아닌, **참조해 사용함으로써 값을 숨길 수 있다.**
```python
# 1.
CONF_DIR = os.path.join(BASE_DIR, '.conf')
config = json.loads(open(os.path.join(CONF_DIR, 'settings_debug.json')).read())

# 2.
EMAIL_HOST = config['email']['EMAIL_HOST']
EMAIL_PORT = config['email']['EMAIL_PORT']
EMAIL_HOST_USER = config['email']['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['email']['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = config['email']["EMAIL_USE_TLS"]
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
*  `conf` 폴더 안의 json값을 불러들여 `config` 안에 집어넣는다. 두 번째 식이 잘 이해가 안 갈 수 있다. 순서를 설명하면,
	1. **`open(os.path.join(CONF_DIR, 'settings_debug.json').read()` open 함수로 파일을 읽는다.(read)** 이때 결과는 단순 문자열일 것이다.
	2. **그 문자열을 `json.loads`함수로 파싱한다.** 그리고 그 값을 `config`라는 변수에 답는다. 완벽한 json 객체가 된다. `load`와 `dump`의 차이, `load`와 `loads`의 차이는 직접 확인해보기 바란다.
* 이메일을 보내기 위한 세팅 값들을 값을 참조해서 쓴다. 이때 실제 내용은 드러나지 않는다.<br><BR>

#### 앞으로 위와 같은 방법을 사용해서 민감한 정보를 가린 채 안전하게 공유할 수 있을 듯 하다.
<br><br><br><br>



# 2 . Photo app의 모델 구축하기.
우리의 프로젝트에는 앱들이 점점 추가되고 있다. 이번에는 `Photo` 앱을 만들었는데 이 앱은 각 유저의 사진앨범과 사진, 그리고 사진에 대한 좋아요 수,  안 좋아요 수를 저장할 것이다.<br>
모델을 4개 만들 것인데 중요한 내용이 있어서 꼭 짚고 넘어가고자 한다. 일단 전체 모델 모듈은 다음과 같다.
```python
from django.conf import settings
from django.db import models
# 1. from django.contrib.auth import get_user_model

class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Album title : {}".format(self.title[:10])


class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='photo')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        through='PhotoLike',
                                        related_name='photo_set_like_users',
                                        )
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           through='PhotoDislike',
                                           related_name='photo_set_dislike_users')

    def __str__(self):
        return "Photo title : {}".format(self.title[:10])

class PhotoLike(models.Model):

    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDislike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
```
개괄하자면 일단 `Album`, `Photo`, `PhotoLike`, `PhotoDislike`의 4개의 모델이 있다. 하나의 앨범은 여러 사진을 가질 수 있으며, 하나의 사진은 좋아요 수, 안 좋아요 수와 연결된다. 하나의 클래스를 각각 살펴보도록 하겠다.

<br>
1. Album
```python
class Album(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Album title : {}".format(self.title[:10])

```
제목과 설명 필드를 가지고 있다. 특기할만한 것은 `owner`로 우리의 모델을 외래키로 갖는다. 즉 **한 명의 유저가 여러 앨범을 가질 수 있는 것이다.**<br>
이떄, `settings.AUTH_USER_MODEL`를 주목해야 하는데, 위에서 우리는 `django.config.settings`를 임포트했다. 
그 모듈을 통해 `settings.py`에 설정한 값들을 가져다가 쓸 수 있다.<br>
 해당 모듈 안 속 `AUTH_USER_MODEL` 변수에 프로젝트의 유저 모델을 설정해놓았다. 그 유저 모델을 외래키로 갖는 것이다.

<br>
2. Photo
```python
class Photo(models.Model):
    album = models.ForeignKey(Album)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='photo')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        through='PhotoLike',
                                        related_name='photo_set_like_users',
                                        )
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                           through='PhotoDislike',
                                           related_name='photo_set_dislike_users')

    def __str__(self):
        return "Photo title : {}".format(self.title[:10])
```
이 모델이 까다롭고 중요하다. 하나씩 살펴보자.<br><BR>

* 하나의 앨범은 여러 사진을 가지고 있다. 그래서 `Photo` 클래스는 `Album`을 외래키로 갖는다.
* 사진에서 소유자가 있으므로, 사용자 또한 외래키로 갖는다.
* 사진 주소를 받는 `ImageField`를 설정한다. 이 필드는 `FileField`를 상속받으며 추가적으로 받은 파일이 이미지인지 검증한다. 그리고 이미지이기 때문에 width, height 속성 또한 갖는다. `upload_to`는 사진이 업로드될 공간이다. 조금 있다가 설명하겠지만 우리처럼 `photo`라고 지정하면 `MEDIA_ROOT/photo`에 사진이 저장된다. `MEDIA_ROOT`은 조금 있다가 다시 설명한다.
* 하나의 사진은 여러 사람으로부터 '좋아요'를 받을 수 있고, 한 사람은 여러 사진을 '좋아요'할 수 있다. 그래서 `ManyToManyField`로 받는다. 그리고 `through` 속성을 통해 `PhotoLike` intermediate 모델을 통해 연결된다. 이때 중요한 것이 related_name.  생각해보자. 외래키든, 다중키든 서로 ORM을 통해 연결될 수 있다. `photo1.owner....`나 `owner.photo_set....`와 같이 말이다.
이상한 걸 느낄 수 있는가? `Photo`는 여러 필드에서 `User`와 연결되어 있다. 
이때, **`user1.photo_set`은 과연, `owner`, `like_users`, `dislike_user` 중 누구와 연결되는가?** 그 관계가 꼬여 있다.
그래서 `related_name` 속성을 써준다. 이렇게 지정해주면 `foo_set`이 아닌 지정한 값으로 연결된 다른 필드를 접근할 수 있다.


<br>
3. PhotoLike & PhotoDislike
```python
class PhotoLike(models.Model):

    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoDislike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
```
사진에 대한 '좋아요', '안 좋아요'를 담을 intermediate 모델이다. 유저와 사진에 외래키로 묶여 있다. 그리고 사진이 생성되면 자동으로 그 날짜를 기록하도록 한다.



<br><br><br><br>
# 3. media setting in DJANGO
우리는 css, sass와 같은 정적인 파일을 `static` 폴더를 통해 관리하고 있었다.<br>
 조금 비슷하지만 다르기도 한, **유저가 업로드한 이미지 파일 등은 어떻게 관리할까?** 사진 또한 정적인 파일이다. `그러면 똑같이 static을 통해 관리하면 될까?`<br><BR>
 
 장고는 보안 등의 이유로 권장하지 않는다. 그 대신, 업로드된 사진, 동영상을 관리할 수 있는 또 다른 방법을 제공하는데 그것이 `media`이다.<br><BR>
 
 먼저 예를 통해 확인하자. `settings.py`에 다음과 같이 적는다.
 
 ```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT은 유저가 업로드한 파일이 저장될 절대경로이다.
#  따로 지정하지 않으면 기본값은 ''(빈 문자열)이다.
# 아까 ImageField에서 upload='photo'라는 속성을 넣어줬다.
# 이 속성의 뜻은 "MEDIA_ROOT + 'photo'", 즉 프로젝트 내 photo 폴더 내에 사진을 저장한다는 뜻이 된다.
# MEDIA_ROOT를 os.path.join을 통해 '기본 경로/media/'로 지정하면 저장되는 장소는 '기본 경로/media/photo'가 된다.


MEDIA_URL = '/media/'
# MEDIA_ROOT와 헷갈리면 안 된다.
# 우리가 MEDIA_ROOT을 통해 사진을 정상적으로 저장했다고 하자. '기본 경로/media/photo'에 사진이 저장되었을 것이다.
# 그런데 admin 사이트로 가서 사의 경로를 확인하면 절대경로가 아닌 'photo'를 포함하는 파일의 상대경로만 지정되어 있다. 
# 그래서 정상적으로 사진 파일을 열어볼 수 없다. 이때 MEDIA_URL을 지정해줘야 한다.
# MEDIA_URL = '/media/'와 같이 입력해줌으로써 url이 향하는 절대경로는 이곳임을 명시해준다. 
# 앞에 '/'가 온 것은 최상단 경로의 media라는 뜻이고, 끝에 '/'가 온 것은 media가 디렉토리라는 것을 말해준다.
```
<br>
그리고 `urls.py`에는 다음과 같이 적는다.
```python
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
`static`이라는 함수를 통해 해당 url 루트로 연결될 수 있는 정규표현식을 담은 리스트를 반환한다. 리스트이기 때문에 `urlpatterns` 리스트와 합쳐 질 수 있다. 바로 합치면 에러가 발생한다.

##### 이렇게 작성해주면 사진이 자연스럽게 저장되고, 또 열어볼 수도 있다.
