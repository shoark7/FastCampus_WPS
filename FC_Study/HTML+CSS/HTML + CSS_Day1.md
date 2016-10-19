# ◈ HTML + CSS
## HTML + CSS basics: Day 1
작성 날짜 : 2016-09-26<br/>

# 1. HTML

### 1.1 HTML이란?

> **HyperText Markup Language**
> 문서가 링크로 이어져 있고(Hyptertext) 태그 등을 이용하여 문서나 데이터의 구조를 명기하는(Mark up) 언어. World Wide Web(WWW)의 웹페이지를 서로 연결하며, 마크업을 통해 웹 페이지의 콘텐츠를 표현한다.


### 1.2. HTML의 기본 구조
```HTML
<!DOCTYPE html>			                          	# 해당 문서가 html파일임을 명시.
<html lang="en">                          			# 주 사용할 언어가 영어.
<head>                              						# html파일에 대한 메타 정보가 들어감.
  <meta charset="UTF-8">                        # 페이지 내의 인코딩은 UTF-8
  <title>Document</title>                       # 문서의 제목.
</head>
<body>                                          # 실제로 보여지는 부분
  
</body>
</html>
```

### 1.3. 주석
> HTML에서는 주석을 `<!--     -->` 안에 적는다.<br/>


### 1.4. 태그의 요소와 속성
> `<body>  </body>` 등은 태그라고 하며 element라고도 한다.
>  태그 안에는 `<body style='color:gray'>  </body>`처럼 태그에 대한 속성값을 넣어줄 수 있다.

> <요소 속성='값'> 내용 </요소> 처럼 사용한다.
> ex) <a href=“http://naver.com”>네이버 홈으로 가기</a>

### 1.5. 절대경로와 상대경로
파일 등의 위치를 지정할 때는 절대경로와 상대경로를 나눠서 지정해줄 수 있다.

> **절대경로 :  실행되는 파일과의 위치를 상관하지 않고 직접적인 경로를 지정해주는 것.**
> ex ) http://www.google.com/12.png

> **상대경로 : 실행되는 파일과의 위치를 고려하여 위치를 지정하는 것.**
> ex) **images/pypy.png**   <- (실행되는 파일과 같은 경로에 'images'라는 폴더가 있고 그 안에 'pypy.png' 파일이 있다.
</br></br>


### 1.6. 블록과 인라인
요소(element)는 크게 블록(block)과 인라인(inline)으로 나뉜다.

### 1.6.1. 블록 요소
> 블록 요소는 해당 요소가 가능한 최대한 너비를 차지해서, 줄바꿈을 가지는 요소이다.
> ex) div, span, p

### 1.6.2. 인라인 요소
> 인라인 요소는 줄바꿈 없이, 기본적으로 자기 자신의 너비만큼만 공간을 차지한다.
> ex> span, strong, mark


* 블록 요소는 인라인 요소를 포함할 수 있지만, 인라인 요소는 블록 요소를 포함할 수 없다.

> ##1.7  HTML 태그들
> ### 1.7.1. `p` 태그.
> 'paragraph'의 약자로서 한 문단을 표시한다. 블록레벨이다. 
> 
> ### 1.7.2. `br`태그
> 'line break'의 약자로 줄을 바꿀 때 사용한다.
>
> ### 1.7.3. 헤드라인 
> 'Headline'의 약자로 h1부터 h6까지 있다. 숫자가 커질수록 작아진다. 이들은 단순히 크기의 문제가 아니며 검색엔진 등이 페이지의 내용을 검색할 때 포함된 내용들의 중요도를 평가하는 기준이 된다.
> ex) `<h1> 낢이 사는 이야기~! </h1>`
>
> ### 1.7.4. 링크
> 링크는 `a`태그를 사용한다. 'Anchor'의 약자라고 한다.  어떤 페이지를 이동할지를 표현하는 `href`속성(hyperlink reference) 이 반드시 들어가야 한다.
> ex) `<a href="http://www.naver.com" target="_blank">네이버 바로 가기</a>`
>
> ### 1.7.5. 이미지
> `img` 태그를 이용한다. `src` 속성에 파일 이름과 경로를 꼭 지정해줘야 한다.
> ex) `<img src=“이미지 경로" width="100" height="200"> `
>
> ### 1.7.6. 목록
> HTML에 사용하는 목록은 크게 `ol`(ordered list)과 `ul`(unordered list)가 있다. `ol`은 말 그대로 숫자 등이 붙는 순서가 있는 목록이고, `ul`은 순서가 없는 목록이다. 이들은 각각의 리스트를 `li`라는 태그로 감싼다.
> ex>
```html
<ul>
  <li></li>
  <li></li>
</ul>
```

> ### 1.7.7. 정의 목록
> `dl`태그를 쓰며 Description list의 약자이다 . `dt`로 개념을 나타내고, `dd`로 정의를 나타낸다.
> ex) `<dl><dt><dd></dd><dt></dl>`
</BR></BR>

.

> ## 1.8. 클래스와 아이디
> **HTML의 태그들은 사용자가 지정한 속성값을 가질 수 있는데 대표적으로 클래스와 아이디가 있다.**

> ### 1.8.1 명명 규칙
> 첫 글자는 알파벳으로 시작해야 하고 두 번째부턴 알파벳, 숫자, '-', '_'를 사용할 수 있다.

> ### 1.8.2. 클래스와 아이디의 차이
> id(아이디)는 페이지에서 딱 한 번만 선언 가능하다. unique한 요소에 사용
> class(클래스)는 한 페이지에서 여러 번 선언할 수 있다. 범용적인 요소에 사용한다.

> 둘은 함께 적용할 수 있다.
> 그리고 클래스와 아이디의 이름을 지을 때는 짧은 것이 최선이 아니며 해당 요소의 의미를 명확하게 나타내줄 수 있으면 좋다.
> ex) `<div class="normal" id="ok"></div>`
</br></br>


# 2. CSS 기본
> ## 2.1. CSS란?
> 마크업 언어가 실제 표시되는 방법을 기술하는 언어. 레이아웃과 스타일을 정의할 때 주로 사용.
>  **HTML이 구조를 잡는다면 CSS는 꾸미는 역할을 한다.**
> **'Cascading Style Sheet'**의 약자로 태그가 중첩되는 HTML을 넘실넘실 넘어가며 스타일이 적용되는 것을 비유적으로 표현했다. 난 그렇게 생각한다. 

> ## 2.2. CSS 문법
> **`selector { property:value;  property:value } `**<br>
>    선택자              속성 : 값                   속성: 값<br>
> ex) **`#body_title{color:red; font-size: 10px;}`**

>## 2.3. CSS 사용법
> CSS를 HTML에 적용하는 방법은 크게 *inline*, *internal*, *external* 세 가지가 있다.
> ### 2.3.1 *inline*
> 이 방법은 **태그 안에 속성 값으로 바로 넣어주는 경우다.**
> ex) `<div style="color:gray">만사형통!</div>`
>
> ### 2.3.2. *internal*
> 이 방법은 **`head` 태그 안에 `style`태그를 넣고 그 안에 작성하는 경우다.**
ex)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <style>
    h1{
      color:gray;
      font-size:15px;
      font-weight:bold;
    }
  </style>
</head>
<body>
  
</body>
</html>
```

> ### 2.3.3. *external*
> 이 방법은 `head` 태그 안에 `link` 태그를 넣어서, **외부 다른 페이지를 참조해서 스타일을 적용한다.**

```html
<html lang="en">
<head> 
  <link rel="stylesheet" href=“style.css>
</head> 
<body> 

```

> ## 2.4. CSS 선택자
> ### 2.4.1 전체 선택자(universal selector)
> `*`로 표현한다. 모든 태그를 나타낸다.
> ### 2.4.2 타입 선택자(type selector)
> `p`, `h1`과 같이 특정 타입을 나타낸다.
> ### 2.4.3. 클래스 선택자(class selector)
> '.'으로 시작하는 선택자.
> ex) `.section{ color:red;}` <-- 'section' 클래스를 나타낸다.
> ### 2.4.4. 아이디 선택자(id selector)
> '#'으로 시작하는 선택자
> ex) #myway{ color: orange;}    <-- 'myway'라는 아이디를 나타낸다.

> ### 2.4.5. 복합 선택자(combinator selector)
> 이 선택자는 자식, 형제 관계를 따져 선택하는 선택자이다. 조금 까다롭다.
> #### 2.4.5.1 하위 선택자
> 특정 태그의 자식을 표현할 때 쓴다.
> ex) `#section ul{ color:red; }` <-- 'section'이라는 아이디를 갖는 태그 안의 `ul` 모든 태그를 나타낸다.
> #### 2.4.5.2. 자식 선택자
> 위의 하위 선택자와는 달리 **직계 자손만을 표현한다.**
> ex) `#section > ul{color:red}` <-- section 아이디의 직계 ul만 적용된다.
> #### 2.4.5.3. 인접 형제 선택자
> **형제 태그 중(sibling) 중 바로 옆에 있는 태그를 가리킨다.**
> ex) `h1+ul {color: yellow}` <-- `h1` 바로 뒤에 있는 `ul` 태그를 가리킨다.
> #### 2.4.5.4. 일반 형제 선택자
> 인접형제 선택자와 달리 해당 태그 옆에 있는 모든 형제를 가리킨다.
> ex) `h1~ul{color: blue;}` <-- `h1` 뒤에 있는 모든 `ul` 태그

> ### 2.4.6. 가상 클래스 선택자, 가상 엘리먼트 선택자
> 이들은 HTML 소스에는 직접 존재하지는 않지만, 필요에 의해 가상의 상태를 나타낼 때 사용한다.
> #### 2.4.6.1 가상 클래스 선택자(Pseudo-classes selector)
> 이 선택자는 특정 태그에 `':'`를 붙임으로써 나타낼 수 있다. ex)
```css
a:link{ color : red }        # 1.
a:hover { color : blue }	 # 2.
a:active { color : orange }	 # 3. 
a:visited { color : black }  # 4.
a:focus { color : violet }	 # 5.
```
> 1번은 `a`가 기본적인 태그일 때, 2번은 마우스가 올라왔을 때, 3번은 클릭되었을 때, 4번은 `a` 태그를 통해 한 번 사이트 방문을 했을 때, 5번은 입력창 등에서 포커스를 받았을 때 이다.

> #### 2.4.6.2. 가상 엘리먼트 선택자(Pseudo-elements selector)
> 이 선택자는 특정 태그에 `'::'`를 붙임으로써 나타낼 수 있다.
```css
p::first-line{font-size:30px; color:red;}
p::first-letter{font-size:100px;}
```
> 위와 같이 특정 엘리먼트의 한 부분을 선택해서 효과를 줄 수 있다.


> ## 2.5. CSS 스타일 적용 우선 순위
> 한 태그의 하나의 속성에 여러 CSS 단위가 적용되면 무엇이 우선 적용될까? 특정도(specify) 값이 높은 순서대로 적용된다.
> 특정도 계산식

> 스타일 | 특정도
> ------ | --------
> inline(인라인) | 1000
> id selector | 100
> class selector | 10
> tag selector | 1 

> **예시! **

> 스타일 | 특정도
> ------ | --------
> `p { color: gray; }`  | 1 
`p:first-line { color: black; }`| 2  			<-- 가상 클래스는 일반 태그와 점수가 같다.
`.wrap { color: black; }` | 10 
`p.wrap { color: black; }`|  11 
`p.wrap>.item { color: black; }`| 22 
`'#wrap { color: black; }` | 100 
`p#wrap { color: black; }` |101 
`<p style=“color: black;”>Example</p>`|  1000

>### 2.5.1 위의 특정도를 무시하는 흑마법 크큭... 
> `!important`
> **이 값이 속성 값에 있으면 요소에 지정된 어떤 특정도도 무시하고 가장 우선순위로 지정된다.**
> ex) p{color: red !important;}
> 이는 유지보수 등에 어려워 가급적 쓰지 않는 것이 좋다.


> ## 2.6. css 서체
> ### 2.6.1. 색상
> `h1 { color : red;} ` <- `color` 속성을 이용.

> ### 2.6.2. 서체 지정
> `body{ font-family : '돋움',  arial, sans-serif`}
> 위와 같이 서체는 `font-family` 속성 안에 넣는다. **서체의 순서대로 우선 적용되며 만약 해당 서체가 없으면 다음 서체가 적용되는 식이다. 그래서 뒤로 갈수록 기본 서체를 적게 된다.**
>
>### 2.6.3. 서체의 기본 종류
>#### 2.6.3.1. serif
>글자에 꺾쇠가 있는 서체. 인쇄물에 많이 사용된다. 
> ex) **바탕, 궁서, Times New Roman**
>#### 2.6.3.2. sans-serif
> 'sans'는 '없음'을 뜻하는 프랑스어. 'serif'이 없는 글자체를 말한다.
> ex) **Arial, 굴림, 나눔 고딕**
>#### 2.6.3.3. monospace
>**고정 폭 서체로 글자들간 구분이 쉬워야 하는 프로그래밍 코드에서 많이 사용.**
>#### 2.6.3.4. cursive
> **필기체**로 꼭 필요한 부분에서만 쓰도록 한다.

> 서체의 모양은 직접 코딩으로 확인해보길 바란다.

> ## 2.7. 글자 크기 
> `font-size` 속성 안에 넣으며 `px`, `em`, `pt` 등의 단위가 있다.
> 
> ## 2.8. 글자 스타일
> `font-style` 속성 안에 넣으며 `italic`, `normal`, `oblique`가 있다.

> ## 2.9. 글자 굵기
> `font-weight` 속성 안에 넣으며 숫자는 100~900 사이, 단어로는 `light`, `normal`, `bold` 등의 단위를 사용할 수 있다.

> ## 2.10. 줄 간격
> `line-height` 안에 표현되며 숫자만 표현할 경우 `font-size`에 곱한 값이 줄 간격이 된다.
> ex) `p {line-height : 1.5}`

> ## 2.11. 문자 꾸미기
> 링크에 밑줄이 쳐져 있는 것을 본 적이 있을 것이다. 이런 설정을 할 수 있다. `text-decoration`을 사용해서 한다. `undersline`, `overline`, `line-through` 등을 값으로 쓸 수 있다.

> ## 2.12. 문자 정렬
> 한 줄에서 왼쪽 정렬, 오른쪽 정렬 등을 할 수 있다. `text-align` 속성을 사용한다. `left`, `right`, `center`, `justify` 등을 값으로 쓸 수 있다.

> ## 2.13. 문자 들여쓰기
>  `text-indent`라는 속성을 통해 문단 등에서 들여쓰기를 할 수 있다. 값은 음수도 받을 수 있으며 음수를 받을 경우 왼쪽으로 튀어 나간다.

> ## 2.14. 대소문자 변환
> 영어 같은 경우 대소문자를 바꿔줄 수 있다. `text-tranform` 속성을 사용하면 된다. 값은 `capitalize`, `uppercase`, `lowercase` 등이 있다.

> ## 2.15. 자간
> `letter-spacing`이라는 속성을 통해 글자간 간격을 조정할 수 있다.

> ## 2.16. 단어 간격
> `word-spacing`을 통해 글자가 아닌, 단어의 간격을 조정할 수 있다.

