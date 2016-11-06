# DJango day 12.

####2016/10/24 월요일.
#### 박성환


# 1. DJANGO EMAIL 송수신
장고 앱을 통해 이메일을 받고 보낼 수 있다. 오늘 기본적인 이메일을 보내는 것을 해보았다.

## 1. 1. 내 도메인으로 메일 보내기
많은 스타트업들이 자신들의 도메인을 통한 메일을 가진 경우가 많은데 이것들은 보통 이메일 서버를 구축한 것이 아니라 특정 서비스를 사용하는 경우가 많다. <br>
선생님이 말씀해주신 건 두 가지가 있다.

### 1.1.1 [worksmobile](https://www.worksmobile.com/kr/)
국내 서비스이다. 무려 네이버가 사내 플랫폼으로 사용하고 있다고 광고하고 있다.<br>
내 도메인을 통한 이메일 송수신은 물론, 메일 보안 향상, 네이버와의 효율적인 연동을 무기로 하고 있다.

### 1.1.2 [gsuite](https://gsuite.google.com/intl/ko/)
구글의 서비스이다. '_비즈니스 용도에 맞게 설계된 Gmail, 문서, 드라이브, 캘린더를 사용해 보세요_'라는 문구에서 알 수 있듯이 기업용 서비스를 제공한다. 유일한 단점은 라이트유저에게도 월 5달러를 과금하는 유료 서비스라는 것이다.

<br>
## 1.2. 장고로 이메일 보내기.
파이썬에서는 smtplib이라는 모듈에서 이메일을 보낼 수 있다. 장고는 그것보다 더 쉽게 '**django.core.mail**' 모듈을 가지고 있다. 이 모듈을 통해서 메일을 보낼 수 있다.<br>
자세한 내용은 [다음](https://docs.djangoproject.com/en/1.10/topics/email/)과 같다.

### 1.2.1. SMTP backend

`backends.smtp.EmailBackend`라는 백엔드에서 이메일 관련 설정을 커스터마이징할 수 있다. <br><BR>기본값은 밑에와 같이 설정되어 있어 이 값들을 `settings.py`에 설정만해주면 메일 보내는 건 매우 쉽다. 


```css
EMAIL_HOST : 이메일 서버 (ex 'smtp.gmail.com')
EMAIL_PORT : 이메일 서버와 소통할 수 있는 포트.(gmail의 경우 537)
EMAIL_HOST_USER  : 아이디
EMAIL_HOST_PASSWORD : 비밀번호
EMAIL_USE_TLS : TLS 사용 여부
EMAIL_USE_SSL : SSL 사용 여부
...
```
이것이 기본 백엔드의 필수 요소이고, 이것을 통해 메일이 메일 서버를 통해 전달된다.
<br><BR>

`settings.py` 안에 다음과 같이 입력한다.
```python

EMAIL_HOST = 'smtp.gmail.com'
# 메일을 호스트하는 서버이다. 우리는 gmail을 사용한다.
EMAIL_PORT = '587'
# gmail과의 통신하는 포트이다.
EMAIL_HOST_USER = '********@gmail.com'
# 발신할 이메일이다.
EMAIL_HOST_PASSWORD = '********'
# 그 메일의 비밀번호.
EMAIL_USE_TLS = True
# 이 설정이 있으면 TLS 보안 방법을 쓴다는 뜻이 된다. TLS의 뜻은 찾아보기 바란다...
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# 사이트와 관련한 자동응답을 받을 이메일 주소로 기본값은 'webmaster@localhost'라고 한다.
```
`settings.py`에 정확히 인수명을 넣어주면 SMTP 백엔드에서 가져다 사용한다.
<br><BR>
이 기본 세팅을 통해서 메일을 보낼 때는 다음 함수를 사용한다.

```python
from django.core.mail import send_mail

send_mail(
	subject,				# 메일의 제목
	message,				# 메일 메시지
	from_email,				# 발신인
	recipient_list,			# 수신인 리스트
	fail_silently=False,	# 발신 실패시 에러 처리 여부
	)
```
실제로 함수를 만들면 다음과 같다.

```python
def send_mail(subject, message, recipient_list=None):
	from django.conf import settings
	default_recipient_list = ['shoark7@gmail.com']
	send_mail(
		subject=subject,
		message=message,
		from_email=settings.EMAIL_HOST_USER, #!
		recipient_list=recipient_list if recipient_list else default_recipient_list
    )
```
위 코드에서 주목할건, 

* from_email=settings.EMAIL_HOST_USER, #!
	- django.conf.settings를 통해 settings.py에 정의된 변수에 접근 가능하다.
	- 그것에 정의된 발신 이메일을 발신자로 설정한다.<br>
	
* recipient_list=recipient_list if recipient_list else
	- 수신인을 설정한다. 여러 명에게 보내고 싶으면 리스트 형태로 적는다.

##### 메일 모듈의 매우 기본적인 기능을 가지고 메일 송신 기능을 만들었다.
##### 추가로, 구글 발신 아이디의 보안설정이 되어 있으면 '인증받지 않은 앱을 통한 접근'이라는 말과 함께 작동하지 않을 수 있다. 이때는 발신 아이디의 보안을 풀어줘야 한다.

<br><br><br>
# 2. DJANGO SMS 송수신
문자 서비스는 선생님이 소개해주신 사이트의 SDK를 통해 구현하였다. [coolsms](http://www.coolsms.co.kr/)라는 서비스로, 지인들에게 구한 좋은 사이트라고 한다.
<br><br>
이곳의 sdk는 UX적으로는 불편하게 찾아가야 했지만 사용법은 매우 간단했는데 나도 가져다가 바로 쓸 수 있었다. 선생님이 충전해주신 계정을 통해 메시지를 보낼 수 있었다.

```python
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP

def send_sms(number, message):
    # set api key, api secret
    api_key = "NCS5805501D*****"
    api_secret = "A86DF83FB2F77AC52F0322A8B1B*****"

    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['from'] = '01029953874' # Sender number
    params['text'] = str(message) # Message

    if isinstance(number, (list, tuple)):
        number = ','.join(number)

    params['to'] = str(number)  # Recipients Number '01000000000,01000000001'

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)
```
해당 SDK는 `pip`를 통해 설치가 가능했다. 위 코드는 sdk안에 제공된 코드를 내 입맛에 맞게 **아주 조금** 수정했다.<br><br>
예를 들어 한 사람이 아닌 다수에게 보내고 싶을 때가 있다고 하자. SDK는 그 경우 이렇게 하라고만 소개하고 있지 구현해놓진 않았다.
그래서 다수에게 메일 보내기를 직접 구현하였다.<br>
문자 보낼 번호가 리스트나 튜플의 형태로 여러 개 왔을 때 하나의 문자열로 이어서 함수에 넣어줘야 문자가 보내진다고 설명에 쓰여 있다.(ex. Recipients Number '01000000000,01000000001')


<bR><BR><BR>
# 3. [django signals](https://docs.djangoproject.com/en/1.10/topics/signals/)
우리의 프로젝트에서 메일, 문자는 댓글을 달았을 때, **다시 말해 Comment 모델의 인스턴스가 생성되었을 때 발신될 수 있도록 하였다.**<br>
이때 사용한 것이 장고의 signals이다. signals란, 장고 프레임워크 내에서 서로 다른 앱들이 특정 이벤트나 액션이 활성화되었을 때 notify 또는 triggered될 수 있도록 돕는 기능이다.<br><br>

다시 말해 특정 상황에서 동시에 혹은 순차적으로 실행될 코드를 정의할 수 있다.<BR>
그 특정 상황들은 크게,

1. 모델의 인스턴스가 생성될 때의 전후,
	- `django.db.models.signals.pre_save` & `django.db.models.signals.post_save`
2. 모델의 인스턴스가 삭제된 때의 전후,
	- `django.db.models.signals.pre_delete` & `django.db.models.signals.post_delete`
3. 모델의 m2m 관계가 변했을 때의 전후,
	- `django.db.models.signals.m2m_changed`
4. request 요청이 시작될 때의 전후,
	- `django.core.signals.request_started` & `django.core.signals.request_finished`
와 같은 4가지가 있다. 물론 더 있으며 [문서](https://docs.djangoproject.com/en/1.10/ref/signals/)를 더 살펴보길 바란다.<br><BR>

문자를 달았을 때는 Blog앱 안의 Comment 모델의 인스턴스가 생성된 것이므로 `django.db.models.signals.post_save`를 사용하면 될 것이다.<br><BR>

Blog 앱 안의 `signals.py`를 만들고 그 안에 다음과 같이 입력한다.
```python
from django.db.models.signals import post_save # 사용할 메서드
from apis.mail import send_mail # 메일을 보내는 함수.
from django.dispatch import receiver
from blog.models import Comment

def send_comment_mail(sender=Comment, instance, **kwargs):
	title = '{} 글에 댓글이 달렸습니다.'.format(instance.post.title)
	content = '{}에 {} 내용이 달렸네요.'.format(
        	instance.created_date.strftime('%Y.%m.%d %H:%M'),
        	instance.content,
    	)
    send_mail(title, content)

post_save.connect(send_comment_mail)
```
그리고 Blog.apps.py에 다음을 입력해줘야 한다.
```python
class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals
```
ready함수에서 아까 만든 `signals.py`를 대기시켜 놓아야 정상적으로 쓸 수 있다.
