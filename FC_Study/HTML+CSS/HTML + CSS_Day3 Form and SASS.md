# ◈ HTML + CSS
## HTML + CSS basics: Day 3
작성 날짜 : 2016-09-28<br/>

# **1. Form tag**
데이터를 입력하거나 전송할 때 사용하는 HTML 요소이다. 프론트와 백엔드를 잇는 중요한 접점이다. **`form` 태그 안에 여러 요소를 넣을 수 있으며 특정 행동을 통해 브라우저(클라이언트)에서 서버로 데이터를 전송할 수 있다.** 중요한 태그이기 때문에 상세히 다룬다.

## 1.1. form의 속성
`form` 태그에 넣을 수 있는 속성은 많지만 꼭 넣어줘야 하는 값들로는`method`와 `action`이 있다.
### 1.1.1. method
> 맥락 상 여기서 **method는 http 프로토콜 위에서 클라이언트와 서버가 데이터를 주고 받는 방식을 말한다.**<br>
> HTTP에서 지원하는 method는 총 8가지가 있는데 HTML에서 지원하는 종류는 **'GET'** , **'POST'** 두 가지이다.<br/>
> GET과 POST의 차이는 'GET'은 쿼리스트링이 URL에 같이 붙어 넘어가고, POST는 그렇지 않다는 것이다. <br>
> 디폴트는 'GET'이기 때문에 만약 로그인 요청 등의 페이지에서는 'POST'를 써야 정보가 안전하게 서버로 넘어갈 것이다.<br>

### 1.1.2. action
> `form`에서 데이터를 전송할 url을 지정한다. 


#### for example
```html
<form action="https://www.naver.com" method="get">  
  <label for="username">ID</label>  
  <input type="text" name="username">  
</form>
```


## 1.2. form의 요소
데이터 전송을 위한 입력을 받는 종류는 굉장히 많다. 평소에 우리가 많이 보는 텍스트필드, 버튼, 체크버튼 등이 모두 `form`의 요소들이다. <br/>
종류가 많고, 그래서 공부를 잘 해야 할 것 같다.

>### 1.2.1. input
> `input`은 `form`의 가장 대표적인 요소이다. 말 그대로 사용자의 입력을 받는다. **`type`이라는 속성을 통해 비밀번호, 글자, 체크박스, 버튼 등의 설정을 할 수 있으며** 다른 유용한 속성도 많다. 다뤄보자.
> #### 1.2.1.1. type
> type에서 입력 수단의 종류를 정할 수 있다. 대표적인 것들을 살펴보자.
```html
1. <input type="text" id="username" placeholder='아이디를 입력하세요.'>  
2. <input type="password" id="password">  
3. <input type="radio" id="radio">  
4. <input type="checkbox" id="checkbox">  
5. <input type="button">  
6. <input type="file" id="file">  
7. <input type="submit">  
8. <input type="reset">  
9. <input type="hidden" id="hidden" value="hiddenValue"> 
```
> 1. `text` : 사용자의 입력을 받는다. 
> 2. `password`: 사용자의 입력 중 비밀번호를 받는다. 입력 시 검은 점으로 가려져서 보인다. `placeholder`라는 속성에 값을 넣으면 입력 전 회색 글씨로 설명이 들어간다. 
> 3. `radio` : 라디오 버튼은 남, 녀 중 성별을 선택하는 것과 같이 버튼 중 단 하나만이 선택가능한 버튼이다. 여러 버튼 중 같은 성격의 버튼이라는 것을 정의하기 위해서는 그 **버튼들의  `name`속성에 같은 값을 부여하면 된다.**
> 4. `checkbox` : `radio`와 달리 다중 선택이 가능하다. 역시 `name`에 같은 값을 넣어줘야 한다.
> 5. `button` : 클릭하는 버튼이 나온다.
> 6. `file` : 생성하면 사용자가 본인의 컴퓨터에서 파일을 올릴 수 있다. 전송 시 해당 경로에서 파일을 찾아 서버에 같이 전송된다.
> 7. `submit` : **이 속성이 들어간 버튼을 누르면 `form` 안에 들어간 모든 입력들이 서버로 전송된다.**
> 8. `reset` : `form` 안의 들어간 입력들을 모두 초기화한다.
> 9. `hidden` : 이 속성을 통하면 보이지 않는 `input`이 된다. 이것의 용도는 사용자에게 보내질 필요는 없는데 서버측에서 `form`과 관련한 특정 상태를 저장해야 할 때 사용한다고 한다.

> #### 1.2.1.2. name
> 이 속성은 `input` 속성의 이름을 특정지어서 **후에 자바스크립트 등에서 참조할 때 사용할 수 있다. 그래서 가능하면 `name` 값을 주면 좋다.** 또한 `radio`, `checkbox`의 경우에는 같은 `name`을 받아야 같은 그룹으로 묶일 수 있다.

> #### 1.2.1.3. placeholder
> 네이버 회원가입 등에 들어가보면 ID를 입력하는 칸에 회색 글씨로 '아이디'라고 보여 사용자가 보기 쉽게 하고 있다. `placeholder`에 값을 주면 그 값이 딱 이렇게 보이게 된다.

> #### 1.2.1.4. checked
> `radio`와 `checkbox`에 해당된다. 어떤 사이트를 들어 갔을 때 선택할 수 있는 버튼은 많지만 대표적인 하나에 미리 표시되어 있는 경우가 있다. 그 `input`에 `checked="checked"` 속성을 주면 디폴트로 선택되어 페이지가 렌더링된다.

> #### 1.2.1.5. maxlength
> `text`, `password` 등의 속성을 갖는 `input`에 이 속성을 주면 주어진 숫자를 넘는 길이를 가진 입력을 할 수 없다.

> #### 1.2.1.6. disabled, readonly
> **이 두 속성은 속성만 입력하고 값은 입력하지 않는다.** `disabled`는 해당 `input`이 흔적만 남고 사용할 수 없게 되며 , `readonly` 속성은 변경은 할 수 없고 읽을 수만 있게 된다.

> #### 1.2.1.7. value
> `text`, `password` 등의 속성을 갖는 `input`에 이 속성과 값을 주면 기본적으로 `value` 값이 들어가 있다.


> ### 1.2.2. select
> ### 1.2.2.1. select
> `select` 요소는 다수의 값 중에서 하나 혹은 소수만 선택할 때 사용한다. 예를 들어, 드롭박스 형태 등을 만들 수 있다.

```html
<select name="" id="">
    <option value="1">a</option>
    <option value="2">b</option>
    <option value="3">c</option>
    <option value="4">d</option>
</select>
```

> 다음과 같이 만들 수 있다. `select` 안에 선택할 수 있는 `option` 요소를 만들 수 있다. 여기서 '1,2,3,4'의 값을 갖는 `value` 속성과 'a', 'b', 'c', 'd'를 구별해야 한다. **실제 화면에서는 영어값이 보이고, 서버로 전송될 땐 `value`의 값이 넘어간다.**

> ### 1.2.2.2. select의 속성
> 또한 `select`의 속성에<br>
> 1.  `multiple='multiple'` 속성값을 넣어주면 여러 개의 옵션을 선택할 수 있다. <br> 
> 2. `size=값' 속성 값을 주면 한 번에 몇 개를 보여줄지를 결정할 수 있다.

> ### 1.2.3. button
> `button`은 `input`의 같은 `type`을 대체할 수 있다.


> ### 1.2.4. fieldset
> `fieldset`은 `form`을 감싸듯 화면에 출력하여 CSS 없이 만드는 화면 중 나름 깔끔하게 만들 수 있다. `fieldset`은 한 번 만들어보길 바란다. ~~이건 놀라웠다...~~
```html
<fieldset>  
  <legend>Login</legend>  
  <label>username : </label><input type="text">
  <label>password : </label><input type="password">
</fieldset> 
```
> 1. `fieldset`이라는 요소로 전체를 감싼다. <br>
> 2. `legend`를 `fieldset`의 첫 번째 자식으로 사용해야 한다.<br>
> 3. `label`로 어떤 값을 받는지 입력한다.



---
# **2. SASS**
## 2.1. SASS란
[SASS](http://www.sass-lang.com/)는 Syntactically Awesome StyleSheet의 약자로, CSS 전처리기(CSS Pre-processor) 중 하나이다. 한 마디로 CSS를 편하게 작성하게 도와주는 컴파일러라고 할 수 있다. <br>
기존 CSS는 문법이 구식이고 그동안 문법적인 변화가 거의 없었기 때문에 작성하기 귀찮고 번거로운 부분이 많았다. <br>
**SASS는 자신의 문법을 통해 CSS 작성을 편하게 해놓고, 자체적으로 컴파일해 CSS로 완전호환되게 만들어준다.**<br/>
문법이 있기 때문에 공부를 해야 한다는 새로운 부담감이 있지만 잘 사용할 경우 코드 효율이 좋은 부분이 있기에 패스트캠퍼스에서 배우게 되었다
SCSS, reset 등 다른 전처리기도 있으니 참고 바란다.

## 2.2. SASS 기본 구조
SASS는 기본 문법이 파이썬과 비슷한 부분이 있다. 또한 OOP의 상속기능, 변수 기능도 있어서 진입장벽이 매우 높지는 않은 편이다.
### 2.2.1. SASS Basic
```SASS
div.container  
// 중괄호를 쓰지 않음
  padding: 15px  
  margin: 0  
   
  p#main-title  
    font-size: 16px  
    font-weight: bold  
   
  .fixed  
    position: fixed  
    bottom: 10px  
    right: 10px
```
문법의 특징을 살펴보면 다음과 같다.
> 1. 속성-값 뒤에 ';'를 적지 않는다. <br>
> 2. ' {} '를 적지 않는다.<br>
> 3. **하위 선택자의 경우 들여쓴다.(space 2칸 정도)**<br>
> -> 위의 경우 `.fixed`는 `div.container  `의 하위에 있는 `fixed` 클래스 요소의 속성을 지정할 수 있다.<br>
이 정도만 알아도 기본적으로는 쓸 수 있다.


### 2.3. SASS -> CSS 변환방법
>스쿨에서 [atom](https://atom.io/) 에디터를 사용하고 있다. 아톰에서 [`sass-autocompile`](https://atom.io/packages/sass-autocompile)이란 패키지를 설치하고, SASS 파일을 만든 뒤 에디터에서 저장하면 원하는 위치에 CSS가 자동생성된다.<br>
>CSS가 생성되는 방식에는 크게 4가지가 있고 사용자가 선택할 수 있다.
	
```css 
/* 1. expanded */
div.container {  
  padding: 15px;  
  margin: 0;  
}
/* 가장 일반적인 표기법으로 W3에서 표준으로 제정하는 방법이기도 하다.*/

/* 2. nested */
div.container {  
  padding: 15px;  
  margin: 0; }  
  div.container p#main-title {  
    font-size: 16px;  
    font-weight: bold; }  
  div.container .fixed {  
    position: fixed;  
    bottom: 10px;  
    right: 10px; } 
/* SASS의 중첩표현이 그대로 드러나는 방법이다. */

/* 3. compact */
div.container { padding: 15px; margin: 0; }  
div.container p#main-title { font-size: 16px; font-weight: bold; }  

/* 하나의 '{ }' 단위를 기준으로 한 줄씩 만드는 방법이다. */

/* 4. compressed */
div.container{padding:15px;margin:0}div.container p#main-title{font-size:16px;font-
weight:bold}div.container .fixed{position:fixed;bottom:10px;right:10px}

/* 극단적으로 완전히 한 줄로 줄이는 방법이다. */
``` 
> 파일을 생성하면 원 SASS 파일의 이름대로 CSS가 생성되는데 expanded만 제외하고 나머지 방법들은 이름에 자신의 이름이 들어간다. <br>
> ex) index.compact.css, index.compressed.css


### 2.4. 문법 추가!
본격적인 문법을 좀 더 알아보도록 하자.
> #### 2.4.1 주석
> `// 주석` 또는 `/* 주석 */`을 사용한다. **전자는 SASS에서만 문제없이 적용되기 때문에 CSS파일에서는  삭제된다. 그리고 한 줄만 주석처리한다.** 후자는 CSS 기본 주석 방법이기 때문에 상관이 없다.

> #### 2.4.2. 문자 셋 설정
> `@charset "UTF-8"` 을 통해 SASS내 쓰인 문자 인코딩 방식을 지정할 수 있다.

> #### 2.4.3. 부모 참조 선택자(&)
> `&`을 통해 부모를 표현할 수 있다. `a` 태그를 만들고 그 안에 유사클래스를 만든다고 할 때 `&:hover`와 같이 표현할 수 있다.

> #### 2.4.4. 중첩 속성
> `margin-left`, `border-left`, `list-style-type` 등과 같이 '-'로 연결된 모든 것은 중첩의 대상이 될 수 있다.

```css
.container  
  margin:  
    left: auto  
    right: auto
```

> 이 때 `margin:`에 ':'가 붙는다는 것만 유의하면 된다.


> #### 2.4.5. 선택자 상속(@extend)
> SASS의 강력한 기능 중 하나이다. 특정 selector를 상속 받게 할 수 있다. 그리고 상속 받는 쪽에서 `@extend`를 써주면 된다.

```css
.btn  
  background-color: #cdcdcd  
  font-weight: bold  
  color: white  
  padding: 5px 20px  
   

.btn-ok  
  @extend .btn  
  background-color: #d9edf7  
   
.btn-cancel  
  @extend .btn  
  background-color: #bbb 
```

> 이렇게 상속을 사용하면 일부만 바뀐 요소를 쉽게 컨트롤 할 수 있다. 
> 그리고 대체선택자라고 불리는 '%'를 `'%btn'`과 같이 쓰면 'btn'은 일종의 추상클래스처럼 사용할 수 있다. 'btn' 자체는 사용할 수 없다.


> #### 2.4.6. 변수($)
> php와 같이 변수를 설정할 때는 이름 앞에 '$'를 붙이면 해당 식별자는 변수가 된다. 자주 쓰는 값을 변수로 설정하면 좀 더 편하게 코딩할 수 있다.

```php
$padding: 10px  
$bg-color: #ececec  
$title-font-weight: bold  
```


> #### 2.4.7. SASS 파일 호출(@import)
> SASS 파일 앞에 `@import 파일이름` 과 같이 입력하면 파이썬에서 모듈 import 하듯이 파일을 그대로 가져와서 사용할 수 있다. <br>
> CSS 파일을 불러올 때는 확장자를 입력해야 하지만, **SASS를 불러올 때는 확장자를 입력하지 않아도 된다.** <br>
> 또한 직접 쓰지는 않고 템플릿처럼 사용할 SASS 파일의 경우에는 파일 이름 앞에 '_'를 붙여서 만들 경우, SASS가 CSS 파일로 변환하지 않는다. 이런 파일을 import해서 사용하면 된다.
