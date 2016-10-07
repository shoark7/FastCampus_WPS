# ◈ Django Day 2.
# 장고 Tutorial 3-4 
<p style='text-align:right'>2016/10/06<br>박성환</p>
## [Tutorial 3: view, errors, templates](https://docs.djangoproject.com/en/1.10/intro/tutorial03/)
**view(이하 뷰)란 일반적으로 특별한 기능과 특별한 템플릿을 갖는 장고 어플리케이션의 웹페이지의 한 종류이다.**

장고에서는 웹피이지와 다른 내용들은 뷰를 통해 전달된다. 각각의 뷰는 간단한 파이썬 함수나 CBV에서는 객체를 통해 전달된다. 장고는 URL을 통해 뷰를 결정할 것이다.
 
 
```python
 urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
 ```
 


1. **url 함수의 첫 번째 인자는 정규표현식, 두 번째는 호출할 뷰, 세 번째는 편하게 부를(나중에 사용할) 이름이다.**
2. **url을 작성할 때 `(?P<question_id>[0-9]+)` 이 표현은 '()' 그룹으로 묶는데 조건에 맞는 값을 'question_id' 변수에 담겠다 라는 의미가 된다. **

뷰를 찾으면 해당 뷰가 다음과 같이 실행된다.

`detail(request=<HttpRequest object>, question_id='34')`




```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

다음은 url을 통해 호출될 `index` 뷰이다.<br>
1. 먼저 `Question` 테이블에서 `pub_date` 필드를 내림차순으로 5개 정렬해 뽑아온 후, <br>
2. 보낼 템플릿을 만든다. 그 템플릿은 `index.html`이다.<br>
3. 템플릿과 `context`라는 딕셔너리 데이터셋을 같이 response로 보낸다.



뷰를 통해 템플릿을 로드하고 컨텍스트를 채운 뒤 응답하는 것은 매우 일상적인(tedious) 작업이기 때문에 위의 코드를 간편하게 만드는 함수도 존재한다.

```python

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'index.html', context)

```
<br>

`render` 함수는 request, 템플릿이 될 페이지, context를 차례로 받은 뒤<br>
1. 페이지를 템플릿으로 로드하고,<br>
2. context과 같이 포장해서<br>
3. response를 보내는 것을 일괄적으로 해준다.
<br>


다음은 index를 통해 접근할 수 있는 detail.html이다.
```python
<h1>{{ question.question_text}}</h1>
<ul>
{%for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
1. detail 뷰에서 해당 id값을 갖는 question을 가져왔다.
2. `h1`은 질문 내용.
3. 하나의 질문은 여러 질문 선택(Choice)를 갖고 있다. `question.choice_set`으로 하나의 질문이 가지고 있는 선택 집합을 가져올 수 있다. <br>
테이블 생성시 `Choice` 테이블에서 `Question`을 직접 필드로 가졌고 `Question`는 그렇지 않았다. 그래서 이것을 '역호출'했다고 한다.
4. `for`문을 통해 하나의 질문의 선택들을 모두 호출하며, 그들의 선택 텍스트를 출력한다.

<br><Br><br>
`<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>`
detail.html을 링크 거는 우리의 이 코드는 문제가 있다. 수많은 템플릿이 있을 때 경로가 하나 바뀌면 모든 템플릿을 수정해줘야 하는 것이다. 이렇게 하드 코딩된 것을 풀어줘야 한다.

`<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>`

이 코드의 'detail'은 아까 우리가 url 함수에서 세 번째 인자:이름으로 넣어준 값이다. 이렇게 `url` 뒤에 이름을 적음으로써 해당 뷰를 바로 불러올 수 있다.


이 방법은 그래 좋다. 근데 문제가 하나 있는데 수많은 app들의 템플릿이 모여 있는데 이들의 이름이 겹치는 경우는 없을까?<br>
그것에 대처하는 방법이 있고 _namespacing_이라고 부른다.<br>
적어도 app 단위에서는 같은 이름이 존재하지 않을 것이다. 루트 url.py에 `include` 함수가 있을 것이다. 세 번째 인자로 'namespace'를 키로 하는 값을 적어준다. 그리고 

`<li><a href="{% url 'polls_name:detail' question.id %}">{{ question.question_text }}</a></li>`

와 같이 'detail'앞에 `polls_name:detail`처럼 붙여준다. **그러면 'polls_name'이라는 네임스페이스의 detail 뷰를 실행한다는 것으로 이해된다.**


<br><br><br><br>
## [Tutorial 4: forms and generic view](https://docs.djangoproject.com/en/1.10/intro/tutorial04/)

투표와 관련한 간단한 `form` 태그를 만들어보자.
```django

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>

```

1. `form`에 대해 먼저 살펴보자. 'action'을 통해 우리는 vote 뷰를 실행하게 될 것이다. 그리고 보내는 방법은 'post'이다
2. `{% csrf_token %}`는 'post'로 `form`을 입력할 때 꼭 넣어줘야 한다고 한다. 'Cross Site Request Forgery'의 약자로 특정 인터넷 공격이라고 한다. 
3. `intput`은 라디오버튼이고, 'value' 값으로 `choice.id`가 들어갈 것이다. 서브밋이 되면 'choice:choice.id' 쌍으로 값이 전달될 것이다.
4. `choice{{ forloop.counter }}`은 템플릿 언어에서 지정하는 것으로 `for`문이 돌 때마다 1, 2, 3, 4식으로 늘어난다.


```django

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

다음으로 `vote` 뷰이다. 'detail.html' 뷰에서는 선택지 중 하나를 선택하고, 'submit'으로 보냈다. `votet`는 그것에 대한 처리를 한다.<br>
먼저 'selected_choice'라는 변수에 request의 'choice' 키에 해당하는 값을 가져온다. 여기서는 choice의 아이디가 된다. <br>
그런데 만약 submit은 했는데 체크를 안 하고 보냈다면, 에러를 일으켜 'error_message'를 보낸다.<br>
정상적으로 하나를 선택해 보냈다면, 그것의 'votes' 값을 1 증가시키고 저장한다. 그리고 결과를 보여줄 `reults` 뷰에 보낸다.
<br> `reverse`는 지정된 네임스페이스를 바로 url로 바꿔주는 역할을 한다. 번거롭게 url을 찾아야 할 필요가 없어진 것이다.<br><br><br>


마지막으로 투표결과를 보여줘야하니 `results`을 설정하자.

```django
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

`results`뷰는 해당하는 question을 가져온 뒤, `results.html` 탬플릿을 렌더링한다.

```python
# results.html

<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

`detail`과 상당히 유사한데, 대신 투표의 숫자까지 가져온다는 점이 눈여겨볼만 하다.<br>
그리고 `{{ choice.votes|pluralize }}`가 굉장히 신기했는데 'vote'가 2 이상이면 's'를 붙여서 복수형으로 표현한다. ~~이건 진짜 어썸~~

저 표현에 문제가 하나있다면, 만약 동시에 두 명 이상의 유저가 'selected_choice'를 받고 거기에 1을 추가했다면 44가 되는 것이 맞지만 43으로 표현될 것이다.<br>
이런 문제를 '[race conditions](https://docs.djangoproject.com/en/1.10/ref/models/expressions/#avoiding-race-conditions-using-f)'라고 한다.
<br><br><br><br>

### Generic view
```python
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question':question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question':question})
```
우리가 아까 만든 뷰이다. 잘 만들었지만 생해보면 생긴 것이 거의 똑같다. 또한 다른 뷰들도 상세한 문법은 달라도 url에 맞게 해당 페이지나 뷰를 호출한다는 것에서는 공통점을 갖는다.<br>
그렇다면 우리는 redundancy가 있다는 것이고 장고는 이것을 줄일 수 있는 방법을 제공한다. 그 중 하나가 뷰를 generic 하게 만드는 것이다. 나도 아직 잘 모르니 계속 보도록 하자.


```python
from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


```
1. 정규표현식을 'pk'로 바꿨다.
2. 뷰를 다른 형식으로 적었다.

```python
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'


def vote(request, question_id):
```
이건 어려워서 다 해석하겠다.<br>
1.  우리는 `ListView`, `DetailView`라는 두 개의 generic view를 사용했다.<br>
각각, '레코드들을 배열로 나열하겠다', '하나의 레코드를 자세하게 보여주겠다'는 의도가 깔려 있다.<br>
2. 각각의 generic view는 자신이 어떤 테이블을 사용할지를 알아야 한다. 이 값은 'model'이라는 속성 안에 넣어준다.<br>
3. `DetailView`는 primary key가 url에서 잡혀들어오길 기대한다. 그래서 우리가 url을 'pk'로 바꿨다.<br>
4. 기본적으로, `DetailView`는 `<app name>/<model name>_detail.html` 이라는 템플릿 이름을 사용한다. 
우리의 경우에는 "question_detail.html"이 되었을 것이다. `template_name`속성을 지정해줌으로써 장고의 자동생성되는 이름이 아닌 우리의 특정한 이름이 될 수 있도록 했다.<br>
5. 유사하게, `ListView`는 `<app name>/<model name>_list.html` 템플릿을 기본적으로 사용한다.<br>
