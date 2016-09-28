# WPS 과제
### 2016-09-28
### 박성환

--- 

## 1. normalize.css, reset.css 알아보기
[normalize.css][normalize], [reset.css][reset]는 설정 초기화를 도와준다. 같은 태그라고 하더라도 브라우저마다 모양이 다른 경우가 많다. 윈도우와 맥의 경우 `button` 등의 모양이나 작동방식이 다른 것을 흔히 알 것이다. <br>
각 도구의 사용법은 CSS 소스코드를 자신의 프로젝트 main.css 최상단에 넣거나, css를 불러올 때 맨 처음 불러오면 된다.

### 1.1. [normalize.css][normalize]
### **A modern, HTML5-ready alternative to CSS resets**
> [깃 허브](https://github.com/necolas/normalize.css/)에서 별을 2만 개를 훌쩍 넘겼다.  Nicolas Gallagher이라는 사람이 만들었고, [이 페이지](https://github.com/necolas/normalize.css/blob/master/normalize.css)에서 보면 확실히 자신만의 스타일로 태그 등을 작성하였다. 페이지에서 말하는 normalize가 하는 일은<br>
> 1. resets.css와 달리 유용한 기본 설정은 보존하고,<br>
> 2. 요소들을 범용성 있게 표준화(normalize)했고, <br>
> 3. 버그와 브라우저간 비호환성을 해결하고자 했으며,<br>
> 4. 미묘한 차이를 내는 사용성을 만드는 요소를 개선하고자 했다.<br>
> 5. 그리고 구체적인 코멘트로 코드가 어떤 일을 하는지 설명한다<br>

코드 자체가 매우 길지는 않았는데 확실히 프레임워크는 아닌 것 같다. 자신이 설정한 각각의 요소마다 왜 그렇게 했는지 구체적으로 설명을 해놓은 것이 인상 깊다.

### 1.2. [reset.css][reset]
### **CSS Tools: Reset CSS**
> 이 초기화 도구는 깃 허브가 없다. [개인 페이지][reset]에서 배포되고 있는데 확실히 주석 등이 없어 normalize.css에 비해 상대적으로 불친절해 보인다. 페이지에서 원작자 Eric Meyer말하는 reset은 <br>
> *리셋의 목표는 line-height, margin과 같은 브라우저간 비호환성 요소를 줄이기 위함이다, 자신은 구체적인 스타일은 지정해주지며 프로젝트에서 커스터마이징해서 쓰기를 권한다, 자유롭게 배포할 수 있다고 말하고 있다*<br>
> 라고 말하고 있다.

최신 버전이 2011년으로 유지보수가 진행되고 있는지 의심스럽다. 쓴다면 깃허브, 트위터, 페이스북 등으로 활발히 검증받고 소통하는 normalize를 쓰고 싶을 것 같다.

## 2. sass mix-in, list 사용법 알아보기

### 2.1. mix-in 사용하기
홈페이지에 [설명](http://sass-lang.com/guide)이 잘 나와 있다. min-in이라고 하면 어려운데 일종의 함수를 만든다고 하면 쉽다. 특정 변수를 넣고 그것에 맞게 원하는 설정을 만들어 모듈처럼 붙여 쓸 수 있다.
```sass
=border-radius($radius)
  -webkit-border-radius: $radius
  -moz-border-radius:    $radius
  -ms-border-radius:     $radius
  border-radius:         $radius

.box
  +border-radius(10px)
```
' =' 을 통해 함수?처럼 요소를 정해준다. 그리고 인자로 들어갈 값을 ' ( )' 안에 넣어준다.(여기서는 `$radius`이다.) <br>
그리고 문법에 맞게 들여쓰고 설정을 해준다. 위에서는 브라우저간 호환을 위한 설정 등을 해주고 있다.
이렇게 설정한 `border-radius`를 원하는 요소 안에서 ' + '를 통해 붙여 쓸 수 있다. 그리고 `$radius`에는 '10px'를 넣어서 모든 브라우저에서 `border-radius`가 10px이 될 수 있게 했다.<br>
참고로, emmet을 통해 브라우저간 설정을 자동으로 편하게 만들고 싶으면 요소 앞에 '-'를 붙이고 TAB을 누르면 된다.<BR>
> ex) `-border-raidus + TAB`


### 2.2. list 사용하기
#####리스트 자체를 만드는 건 쉽다. 다만 어떤 글에서는 SASS에서의 list가 너무 관대해서 그것이 문제라고 할 정도로 자유도 높은 것 같다.
#### 2.2.1. 리스트 만들기
변수 뒤에 인자를 계속 쓴다. 인자 사이는 공백을 써도 되고, 콤마를 써도 된다. 또한 문자열의 경우 공백이 없다면 ' " " ' 를 생략해도 된다.
```
$list-space: "item-1" "item-2" "item-3";
$list-comma: "item-1", "item-2", "item-3";
nth($list-comma, $index)
// 와 같이 사용해서 인덱스에 있는 값을 불러올 수 있다. 정말 다양한 함수가 있다. 더 살펴보길 바란다.

```

단, 공백과 콤마를 섞어 쓰면 다중 배열을 만드는 것처럼 인식되니 조심한다.

<br><br>
출처
1. http://kay.starian.kr/23<br>
2. https://github.com/necolas/normalize.css/<br>
3. http://meyerweb.com/eric/tools/css/reset/<br>
4. http://hmmim.tistory.com/26<br>
5. http://sass-lang.com/<br>
6. http://hugogiraudel.com/2013/07/15/understanding-sass-lists/<br>



[normalize]:https://necolas.github.io/normalize.css/
[reset]:http://meyerweb.com/eric/tools/css/reset/
