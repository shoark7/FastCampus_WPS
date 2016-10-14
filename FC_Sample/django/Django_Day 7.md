# Django Day 7.
#### 2016/10/14
#### 박성환
<Br>
오늘부터 장고의 기본을 마치고 본격적인 개인 연습을 시작하게 되었다. 한영 샘이 내주신 개인 실습과제는 Video 프로젝트! <br><br>
이 프로젝트는
-  간단하게 유투브 동영상에 대한 정보를 담고,
-  그 리스트를 모두 출력한다음,
- 사용자가 하나를 클릭하면 영상과 함께 자세한 정보를 제공하는 프로젝트이다.<br>
지금 모두 구현하지는 못했고, 일부 구현했는데 적은 코드와 유의할 점, 느낀 점을 이야기하겠다.
<Br>

아직 완성되지 않았으며 과제는 다음과 같은 기능을 가지고 있다. 
#### 14일 현재까지 구현 정도 
```

Video project 
 │
 ├  Model				     ┌ 힙합
 │	  ├	Video category ├ 클래식
 │	  │				   └ 레퀴엠
 │      │		   ┌  Uploader
 │	  └ Video	   ├ Title
 │	     		 ├ VideoCategory(Foreignkey!!)
 │		  	     ├ Url
 │			     ├ Usercount
 │			     └ LIkecount
 │
 ├ 	VIew
 │		├ video_list
 │		├ video_detail
 │		├ video_add
 │		└ video_update
 │
 └ Template
  	├ base.html
    ├ video_detail.html
	└ video_update.html
  
 
* 미구현 목록:
	- 모델 : User
	- View: 로그인, 로그인 상태 유지, 좋아요 기능
 		
```

이 중 디버그 시간에 오래 걸리거나, 깨달음을 준 부분을 집중적으로 소개하겠다.
<br><br>

### 1. 모델 섹션
```python
class VideoCategory(models.Model):
    video_category = models.CharField(max_length=30,)
    # 동영상의 장르를 저장한다.
     # Video 모델에서 Foreign Key로 참조한다.
    

    def __str__(self):
        return self.video_category


class Video(models.Model):
"""
실질적으로 유투브 동영상에 대한 정보를 저장하는 모델이다.
여러 필드를 가지고 있는데,
핵심은 `VideoCategory`필드. VideoCategory 모델을 ForeignKey로 참조한다.
`watch_count`는 처음에는 영상 조회수를 구현하려고 했으나,  나중에는 사이트 클릭 수로 바뀌었다.

"""

    uploader = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    VideoCategory = models.ForeignKey(VideoCategory)
    url = models.URLField(max_length=100)
    watch_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

```


### 2. View 섹션

#### 2.1. video_list
```python
def video_list(request):
    lists = Video.objects.order_by('-watch_count')
    context = {
        'lists':lists,
    }
    return render(request, 'video_rank/video_list.html', context)
```
비디오의 목록을 출력한다. 매니저의 `order-by` 함수로 'watch-count'를 기준으로 내림차순 정렬했다. 그 리스트를 context에 담아 `videl_list.html`에 보낸다.

<br>
#### 2.2. video_detail
```python
def video_detail(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except:
        return HttpResponse('그런 비디오는 없습니다.')

    video.watch_count += 1
    video.save()
    context = {
        'video':video,
    }
    return render(request, 'video_rank/video_detail.html', context)
```
한 비디오를 클릭했을 때 그 비디오에 대한 정보를 받는다.
`Video.objects.get(pk=video_id)`에서 `get`은 하나의 인스턴스만 출력하고 같이 없거나 두 개 이상 매치되면 에러를 출력한다. 그래서 예외 구문을 넣었다.



<bR>
#### 2.3. Video_add
```python
def video_add(request):
    context = {}
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_rank:video_list')
    else:
        return render(request, 'common/add.html', {'form':VideoForm()})

    return redirect('video_rank:video_list')
```
새로운 영상을 목록에 추가하는 함수이다. `form`은 ModelForm을 상속받는 `VideoForm`으로 페이지에 폼을 띄우고, 그것에 맞게 저장한다.

<br>

#### 2.4. video_update
```python
def video_update(request, video_id):
    # print(video_id, 1)
    video = Video.objects.get(pk=video_id)

    if request.method == 'POST':
        form = VideoForm(data=request.POST, instance=video)
        if form.is_valid():
            updated_video = form.save(commit=False)
            updated_video.uploader = request.POST['uploader']
            updated_video.title = request.POST['title']
            updated_video.VideoCategory = VideoCategory.objects.get(id=request.POST['VideoCategory'])
            # updated_video.VideoCategory = request.POST['VideoCategory']
            updated_video.url = request.POST['url']
            updated_video.save()
        return redirect('video_rank:video_detail', video_id=video.id)

    else:

        return render(request, 'video_rank/video_update.html', \
                      {'video' : video, 'form':VideoForm(instance=video)})
```
여기가 힘들었는데
`updated_video.VideoCategory = VideoCategory.objects.get(id=request.POST['VideoCategory'])`
이게 중요하다.<br>
**`VideoCategory`는 외래키이다. 그래서 `uploader`, `title`는 바로 POST로 뽑아냈는데 `VideoCategory`는 그냥 뽑으면 외래키의 ID 값이 나온다. 그래서 그 키값을 다시 카테고리 필드의 키로 사용해 장르를 가져왔다.**
<br><BR><BR>

### 3. Templates

#### 3.1. base.html
```django
{% load staticfiles %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>영화 보러 오세요 ㅎ.</title>
    <link rel="stylesheet" href="{% static 'css/common.css' %}">
</head>
<body>
    <div class="nav-bar">
      <div class="center" style="float:left"><a href="{% url 'video_rank:video_list' %}">안녕하세요!</a></div>
      <div class="button-bundle">
        <div class="menu"><a href="{% url 'video_rank:video_add' %}">음악 추가</a></div>
      </div>
    </div>

    <div class="main-part">
    {% block content %}

    {% endblock %}
    </div>

</body>
</html>
```
기본이 되는 base이다. 
1. `{% load staticfiles %}`를 통해 정적인 파일을 로드하겠다고 선언한다.<br>
2.   `<link rel="stylesheet" href="{% static 'css/common.css' %}">`를 통해 static 폴더 밑에 있는 'css/common.css' 파일을 불러 쓰게 된다.

<br>
#### 3.2. video_list.html
```django
{% extends 'common/base.html' %}

{% comment %}
'lists'라는 컨택스트가 넘어옴.
{% endcomment %}

{% block content%}

{% for video in lists %}
<h4><a href="{% url 'video_rank:video_detail' video_id=video.id %}">{{ video.title }}</a></h4>
<p>{{ video.url }}</p>
<p>{{ video.uploader }}</p>
<p>{{ video.VideoCategory }}</p>
<p>{{ video.watch_count }} pe{{video.watch_count|pluralize:'rson,ople' }}</p>
{% endfor %}


{% endblock %}
```
1. 템플릿에서 일반 html, pytho의 주석을 쓸 수 없다. 주석을 넣으려면 `{% comment %}'lists'라는 컨택스트가 넘어옴.{% endcomment %}`처럼 태그 안에 넣어줘야 한다.
2. `<p>{{ video.watch_count }} pe{{video.watch_count|pluralize:'rson,ople' }}</p>`
이건 재밌다. 본 사람이 단수, 복수일 때 구분해주기 위해 했다. 1명 일때는 'person', 2명 이상일 때는 'people'이 될 것이다. 0명일 땐 뭐가 나올까? 해봐라 ㅋ
`

<br>
#### 3.3. video_update.html

```django
{% extends 'common/base.html' %}

{% block content%}

<form action="{% url 'video_rank:video_update' video_id=video.id %}" method="POST">
    {% csrf_token %}

    {{ form.as_p }}
    <button type="submit">제출</button>
</form>


{% endblock%}
```
`form`안 에 `    {% csrf_token %}`를 넣는 것을 잊지 말자.

<br>

#### 3.4.  add.html
```django
{% extends 'common/base.html' %}

{% block content%}

<form action="{% url 'video_rank:video_add' %}" method="POST">
    {% csrf_token %}

    {{ form.as_p }}
    <button type="submit">제출</button>
</form>


{% endblock%}
```

정말 초라하고 못났지만, 내가 직접 만든 것이라 의미 있다.
삭제, 동영상 삽입도 넣더록 하겠다.
