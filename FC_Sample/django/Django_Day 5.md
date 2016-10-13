# Built-in template tags and filters

이 문서는 장고의 template `tag`(이하 태그)와  `filter`(이하 필터)에 대해 다룬다. 
또한 커스텀  태그, 필터의 문서화도 다루기 때문에 당신이 [automatic documentation](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/admindocs)를 사용한다면 유용할 것이다.

<br>
## 1. _Built-in `tag` reference_

### 1.1. autoescape
현재 자동 이스케이핑 작동방식을 제어한다. 'on'과 'off' 두 값을 받으며 이 값이 auto-escaping이 블락 내에서 유효한지 아닌지를 결정한다. 블락은 `endautoescape` 태그로 끝난다.<br><Br>

auto-escaping이 유효할 때는, 모든 컨탠츠가 결과를 출력하기 전에 HTML 이스케이핑이 적용된 상태가 된다. 이스케이핑의 유일한 예외는 `safe`라고 강조된 변수들이다.

```python
{% autoescape on %}
    {{ body }}
{% endautoescape %}
```

### 1.2. block
화면에서 메뉴바 같이 변하지 않는 부분을 그대로 두고 변하는 바디 부분만 건드리고 싶으면 관례적으로 쓰이는 `base.html`에 고정 부분과 함께 가변적인 _**block**_을 지정한다.

```html
{% extends 'blog/base.html' %}   

{% block 블락이름 %}
<div class="post">
    {% if post.published_date %}
    <div class="date">
        <h1>{{ post.title }}</h1>
        <p1>{{ post.text|linebreaksbr }}</p1>

    </div>
    {% endif %}

</div>
{% endblock 블락이름 %}
```
1. `base.html`를 확장한다. `base.html`에 _블락이름_으로 지정된 부분에 이 부분을 끼워넣게 된다. 
2. 블락을 마칠 땐 `endblock`을 쓴다. `endblock` 뒤에 _블락이름_은 생략가능하다.


### 1.3. comment 
파이썬 코드가 들어간 HTML 파일에서 본연의 `<!-- -->` 주석을 쓰면 에러가 뜬다. 주석을 쓰려면 `{% comment %}`, `{% endcomment %}` 태그를 사용하고, 그 안의 모든 문장은 처리되지 않는다. <br><Br>

추가적인 설명을 덧붙이려면 `optional note`를 첫 태그에 집어넣을 수 있다.

```django
<p>Rendered text with {{ pub_date|date:"c" }}</p>
{% comment "Optional note" %}
    <p>Commented out text with {{ create_date|date:"c" }}</p>
{% endcomment %}
```
`comment` 태그는 중첩될 수 없다.

### 1.4. csrf_token
**POST**메서드를 사용하는 html `form`에 꼭 넣어줘야 한다.<br>
Cross Site Request Forgery의 약자로 인터넷 공격의 한 종류라고 한다. 그 공격을 막기 위해 꼭 넣어줘야 한다. 넣지 않으면 에러가 뜬다. 이 태그를 넣으면 `form`안에 내부적으로 _hidden_ 속성을 갖는 버튼이 생성된다고 한다.

### 1.5. cycle

이 속성은 `cycle`과 맞닥뜨리면 인자를 하나씩 불러내는 태그이다. 일종의 리스트의 원소들을 하나씩 호출하는 것 같다. 처음에는 첫 번째 인자를 내놓고, 두 번째 맞닥뜨리면 두 번째 인자를 내놓는다. 루프를 한 번 다 돌면, 다시 처음부터 돌린다. 이건 봐야 이해가 된다. 

```python
{% for o in some_list %}
    <tr class="{% cycle 'row1' 'row2' %}">
        ...
    </tr>
{% endfor %}
```
보통 `for`문과 많이 쓰이는데 `for`문이 한 번 쓰일 때마다 `cycle` 태그와 한 번씩 조우할 것이다. 이때 인자 `row1`, `row2`가 하나씩 순서대로 값을 내놓는다. 그리고 그 흐름은 `for`문이 끝날 때까지 계속된다.<br><BR>

위의 예제에서는 문자열이 인자가 됐지만 변수를 받는 것도 가능하다.
```python
{% for o in some_list %}
    <tr class="{% cycle rowvalue1 rowvalue2 %}">
        ...
    </tr>
{% endfor %}
```
이 때 `rowvalue1`, `rowvalue2`은 변수가 된다.<br><BR>

인자가 바뀔 때마다 같은 값으로 참조하고 싶다면 `as`를 사용한다.
```python
<tr>
    <td class="{% cycle 'row1' 'row2' as rowcolors %}">...</td>
    <td class="{{ rowcolors }}">...</td>
</tr>
<tr>
    <td class="{% cycle rowcolors %}">...</td>
    <td class="{{ rowcolors }}">...</td>
</tr>
```
`'row'`, `'row2'`모두 `rowcolors`라는 대리 변수를 통해 접근하게 되었다.
결과는 다음과 같다.

```python
<tr>
    <td class="row1">...</td>
    <td class="row1">...</td>
</tr>
<tr>
    <td class="row2">...</td>
    <td class="row2">...</td>
</tr>
```
결과에 주의하자. **`cycle` 태그과 부닥치지 않는 한 값 자체는 변하지 않는다. 하지만 이름은 언제나 `rowcolors`로 동일하다.**


### 1.6. extends
해당 템플릿이 부모 템플릿을 확장한다는 것을 표현한다. 사용방법은 두 가지이다.<br>
1. `{% extends "base.html" %}`와 같이 " "를 사용해서 그 이름을 갖는 템플릿을 확장하는 방법이다.<br>
2. `{% extends variable %}`는
  * 변수가 문자열이라면 장고가 그 문자열을 템플릿의 이름으로 사용하며,
  * 변수가 템플릿이라면, 장고는 그 객체를 부모 템플릿으로 사용할 것이다.

<br>
문자열 인자는 path를 상대적인 경로로 지정할 수 있다.

```python
{% extends "./base2.html" %}
{% extends "../base1.html" %}
{% extends "./my/base3.html" %}
```
'`./`'는 현재 경로, '`../`'는 이전 경로, '`./my/`'는 현재 경로 안의 'my' 파일 안에서 템플릿을 찾겠다는 의미이다. 1.10 버전에서 추가되었다고 한다.

### 1.7. filter
필터는 하나 혹은 여러 필터를 포함하는 블락 안의 내용이다. 다수의 필터가 pipe(`|`, 달러키 + Shift)로 연결되어 표현되며, 필터는 인자를 가질 수 있다.<br><BR>

`filter`와  `endfilter` 태그 안에 내용이 들어간다.
```python
{% filter force_escape|lower %}
    This text will be HTML-escaped, and will appear in all lowercase.
{% endfilter %}
```
이 블록은 `force_escape`과 `lower` 인자를 갖고 있으며,<BR>
1. esacpe을 강제한 다음(force_escape),<BR>
2. 소문자로 글자를 표현한다.(lower)

### 1.8. firstof
False가 아닌 첫 번째 인자를 반환한다. 모든 인자가 False일 경우 반환값은 없다.
```python
{% firstof var1 var2 var3 %}
```
아래 식과 동일하다.<br>

```python
This is equivalent to:

{% if var1 %}
    {{ var1 }}
{% elif var2 %}
    {{ var2 }}
{% elif var3 %}
    {{ var3 }}
{% endif %}
```
<br>

그리고 모든 인자가 False일 때 반환할 fallback 값도 지정할 수 있다.
```python
{% firstof var1 var2 var3 "fallback value" %}
```
<br>


### 1.9. for
배열을 순환하면서 context 변수로 들어온 값을 사용한다. 예를 들어 운동선수 목록에서 한 명씩 추출한다고 하자.

```python
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```
`{% for obj in list reversed %}`로 넣어서 리스트를 뒤집어서 넣을 수 있다.<br><BR>

딕셔너리가 들어갈 때는 `items` 메서드를 통해 키, 값 튜플쌍으로 만들고 `key`, `value`로 접근할수  있다. 파이썬 일반 사용법이다.<br>
**다만 템플릿 태그에서 함수에 `( )`를 쓰지 않는다. 함수, 메서드명만 적으면 된다.**
```python
{% for key, value in data.items %}
    {{ key }}: {{ value }}
{% endfor %}
```
<bR>
태그에서 `for`문의 경우 추가로 사용할 수 있는 변수들이 있다.


Variable | Description
--- | ---
forloop.counter | 루트가 몇 번째인지. 1부터 시작.
forloop.counter0 | 루트가 몇 번째인지. 0부터 시작.
forloop.revcounter | 루트의 끝에서 몇 번째인지. 끝이 1번
forloop.revcounter0 | 루트의 끝에서 몇 번째인지. 끝이 0번
forloop.first | 루프의 첫 번째이면 True
forloop.last | 루프의 마지막이면 True
forloop.parentloop | 루프가 중첩된 경우, 현재를 감싸는 부모 루프


### 1.10. for ... empty
`for`태그는 추가로 `empty` 태그를 갖는데 이 태그 블락은 주어진 배열이 비었거나, 찾을 수 없을 때 실행된다.

```django
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>Sorry, no athletes in this list.</li>
{% endfor %}
</ul>
```
`if`, `for` 태그를 중첩해서 똑같이 구현할 수 있지만 이 방법이 훨씬 깔끔하다.


### 1.11. if

`{% if %}` 태그는 조건식 변수를 평가하고, 변수가 True이면 해당 블록을 실행한다.
파이썬 `if-elif-else` 문과 매우 유사하다.

```django
{% if not athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}
```
블락 끝에 `{%endif%}`을 잊지만 않으면 된다. 식 안에는 `and`, `or`, `not`, `is`를 사용할 수 있다.

### 1.12. load
커스텀 템플릿 태그셋을 로드한다. 예를 들어, 다음 템플릿은 `somelibrary`와 다른 패키지의 `otherlibrary`를 로드할 것이다. 여러 개일 경우 띄어쓰기로 접근한다.(' ,' 가 아니다.)

```django
{% load somelibrary package.otherlibrary %}
```
<br>

또한 선택적으로 라이브러리의 개별적 필터나 태그를 로드할 수 있는데 이때 `from`을 사용한다. 일반적인 `from ... import ...` 구문과는 순서가 다르다.

```django
{% load foo bar from somelibrary %}
```



### 1.13. now
주어진 문자열로 이루어진 포맷을 통해 현재 날짜와 시간까지도 표현한다. 이 문자열은 'format specificer' 문자를 포함한다.

```django
It is {% now "jS F Y H:i" %}
```
format과 상관없는 문자들을 raw 문자로 쓰고 싶으면(escape하려면) `\`, 백슬래쉬를 사용한다. 
<br>

```django
It is the {% now "jS \o\f F" %}
```
결과는  “It is the 4th of September”일 것이다. 'o', 'f' 같은 순수 문자열이 백슬래쉬로 이스케이프되었다.<br><BR>

전해지는 포맷은 미리 정해진 값을 넣어줄 수도 있는데 그 값들은 _DATE_FORMAT, DATETIME_FORMAT, SHORT_DATE_FORMAT, SHORT_DATETIME_FORMAT_가 있다.<br>
그리고 이 포맷들은 현지화 정도나, 지역설정에 따라 상이할 수 있다.
```django
It is {% now "SHORT_DATETIME_FORMAT" %}
```
<br>
 
```
{% now "Y" as current_year %} 
```
이렇게 사용해서 포맷의 `Y`, 즉 연도만 `current_year`라는 변수에 넣을 수 있다.



### 1.14. spaceless
HTML 태그 사이의 whitespace를 제거한다. 탭과 new line을 포함한다.

```django
{% spaceless %}
    <p>
        <a href="foo/">Foo</a>
    </p>

{% endspaceless %}
```
요것이
↓↓↓↓↓↓↓↓↓↓↓<br>
```html
<p><a href="foo/">Foo</a></p>
```
이렇게 표현된다. 태그 사이의 공백문자만 없어지고, 태그와 텍스트 사이의 공간은 없어지지 않는다.


### 1.15 url
주어진 뷰와 선택인자들을 매칭하는 URL의 도메인 없는 절대경로를 반환한다. 
이것은 템플릿마다 url을 하드코드해서 DRY 원칙을 망치지 않으면서 링크를 반환하는 방법이다.
```django
{% url 'some-url-name' v1 v2 %}
```
* 첫번째 인자는 url 이름이다. 문자열일 수도, 다른 context 값일 수도 있다. 추가 인자는 선택적이며 스페이스로 구별해야 한다. 위의 방법은 위치 인자를 전달하고 있다. 키워드로 보낼 수도 있다.<br>

```django
{% url 'some-url-name' arg1=v1 arg2=v2 %}
```
위치인자와 키워드 인자를 같이 사용하면 안 되며, URLconf에 필요한 모든 인자는 준비되어 있어야 한다.
<br>



<br><br>
## 2. Built-in filter reference¶

### 2.1. add
인자를 value에 더한다.
```django
{{ value|add:"2" }}
```
값이 4라면, 결과값은 6이될  것이다.<br>
이 필터는 두 인자를 정수로 만들려고 할 것이고, 문자 등에도 마찬가지이다. 어떻게든 처리할수  없는 형태 일때(ex: "나도숫자^^"), 결과는 빈 문자열이 될 것이다.
<br>
```
{{ first|add:second }}
```
`first`= [1, 2, 3], `second`= [4, 5, 6] --> [1, 2, 3, 4, 5, 6]


### 2.2. addslashes
`" " ` 앞에 `\` 를 붙인다. CSV 파일을 이스케이프할 때 유용하다.
```django
{{ value|addslashes }}
```
 "I'm using Django" --> "I\'m using Django"


### 2.3. capfirst¶
값의 앞 글자를 대문자로 만든다. 첫 글자가 문자가 아니면(정확히는 영어가 아니면) 영향이 없다.

```django
{{ value|capfirst }}
```
"django" --> "Django".


### 2.4. center
값을 주어진 너비의 가운데로 보낸다.
```django
"{{ value|center:"15" }}"
```
"Django" --> "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Django&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"

### 2.5. default

value가 False인지 검사하고, 맞으면 주어진 값을 준다. True일 때는 그냥 `value` 본연의 값을 받는다.
```django
{{ value|default:"nothing" }}
```
value가 ""이면(빈 문자열이면), 결과는 'nothing'일 것이다.


### 2.6. dictsort
딕셔너리의 리스트를 받아서 인자의 키로 정렬된 리스트를 반환한다.

```django
{{ value|dictsort:"name" }}
```
이런 식이 있다고하자 .<br><br>

원래 값은 다음과 같다.<br>
```django
[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]
```
결과는 다음과 같을 것 이다.
```django
[
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
    {'name': 'zed', 'age': 19},
]
```
이름 순으로 정렬됐음을 알 수 있다. 더 복잡한 것도 할 수 있 다.<br><BR>

다음과 같은 `books` 리스트가 있다고 하자.
```python
[
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
]
```
<br><BR>
정렬하면 결과는 다음과 같다.
```django
{% for book in books|dictsort:"author.age" %}
    * {{ book.title }} ({{ book.author.name }})
{% endfor %}
```
<br>↓↓↓↓↓↓↓↓↓↓↓↓<BR>
```
* Alice (Lewis)
* 1984 (George)
* Timequake (Kurt)
```
나이순으로 정렬됐음을 알 수 있다.


### 2. 7. first¶
리스트의 첫 번째 아이템을 가져온다.
```
{{ value|first }}
```
value가  ['a', 'b', 'c']라면, 결과는  'a'가 될 것이다.



### 2.8. last
리스트의 마지막 아이템을 가져온다.
```
{{ value|last }}
```
value가  ['a', 'b', 'c']라면, 결과는  'c'가 될 것이다.

### 2.9. get_digit
주어진 자리수의 숫자값을 내놓는다. 맨 오른쪽이 1 이 되고, 그 다음 왼쪽이2가  되는식이다. 인풋이 정수가 아니거나 1보다 작으면 원래 값을 반환한다. 
```django
{{ value|get_digit:"2" }}
```
value가 123456789이면 결과는 8이 된다.




### 2.10. length
값의 길이를 반환한다. 문자열과 리스트 모두작동 한다.
```
{{ value|length }}
```
값이 ['a', 'b', 'c', 'd']나 "abcd"면, 결과는 4가 될 것이다.


### 2.11. linebreaks
평문의 '\n'을 적절한 HTML 태그로 바꾼다. 단일 newline은 `<br />`이 되고, newline 뒤에 빈 줄이 따르는 경우 `<p>`가 된다.
```django
{{ value|linebreaks }}
```
값이 'Joel\nis a slug'이면, 결과는 '<p>Joel<br />is a slug</p>'가 된다.


### 2.12. linebreaksbr
모든 newline을 `<br>`로 바꾼다.
```django
{{ value|linebreaksbr }}
```
값이 'Joel\nis a slug'이면, 결과는 'Joel<br />is a slug'가 된다.


### 2.13. lower¶

문자열을 소문자로 만든다.

### 2.14.upper
문자열을 대문자로 만든다.


### 2.15 pluralize
영어에서 값이 1이 아닐 때 복수 접미사를 붙여준다. 기본값은 's'다.

```django
You have {{ num_messages }} message{{ num_messages|pluralize }}.
```
만약 num_messages이 1이면, 결과는 'You have 1 message'가 되지만 2일 때는 'You have 2 messages'가 된다.<br>
복수 접미사가 's'가 아닌 경우 값을 설정할 수 있다.

```django
You have {{ num_walruses }} walrus{{ num_walruses|pluralize:"es" }}.
```
<br>
까다로운 단복수의 경우 이렇게도 가능.
```django
You have {{ num_cherries }} cherr{{ num_cherries|pluralize:"y,ies" }}.
```


### 2.16. wordcount
단어의 개수를 반환한다.
```django
{{ value|wordcount }}
```
"Joel is a slug" --> 결과는 4가 된다.




