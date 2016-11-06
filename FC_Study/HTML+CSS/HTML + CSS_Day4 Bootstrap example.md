# ◈ HTML + CSS
## HTML + CSS bootstrap: Day 4
작성 날짜 : 2016-09-29<br/>

### 코드 설명
어제와 오늘 [부트스트랩](http://bootstrapk.com/)에 대해 간단히 살펴보고 오늘 본격적으로 실습을 했다.<br>
[다방](https://www.dabangapp.com/)의 홈페이지를 부트스트랩으로 구현을 했는데 완성되지는 않았다. 내일 마무리할 것 같다.<br><br>


먼저 html 파일이다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../bootstrap/css/bootstrap.css">
  <!-- 링크를 통해 부트스트랩 css를 불러온다.  -->
  <link rel="stylesheet" href="css/dabang.css">
  <title>Document</title>
</head>
<body>
  <nav class="navbar navbar-default navbar-no-margin">
  <!-- navbar클래스를 통해 'nav'가 네비게이션을 선언한다.
       navbar-default는 navbar의 테마로 가장 기본적인 네비게이션바이다.
     회색 배경에 검은 글씨가 나온다. navbar-inverse로 색전환을 하면 검은 바탕에 흰 글씨가 나온다,
       navbar-no-margin을 통해 navbar 밑에 마진 공간이 생기는 것을 막는다.
    -->


    <div class="container-fluid">
  <!-- 부트스트랩은 사이트 콘텐츠를 감싸고 그리드 시스템을 만들 콘테이너를 가지고 있다.
       콘테이너에는 container, container-fluid 두 종류가 있다.
     1. container : 반응형 고정폭. 일정 수준의 해상도에서 고정된 길이를 갖는다.
     2. container-fluid : 뷰포트 끝까지 늘어난다. -->

      <div class="navbar-header">
  <!-- 네비게이션의 헤더 부분을 묶는다. -->
        <a href="" class="navbar-brand">
  <!-- 네이게이션의 로고 등을 박기 위한 영역이다. 고정된 폭과 너비를 가지고 있다.
      사용자의 사진의 필요에 따라 속성을 오버라이드 해야 할 필요도 생길 수 있다.-->

          <img src="images/logo.png" alt="로그쨔응~">
  <!-- 이미지를 가져오는 태그. alt속성은 src의 이미지를 불러올 수 없을 때 나오는 텍스트로
      html 표준에서 꼭 입력하라고 강조하고 있다. -->
        </a>
      </div>

      <ul class="nav navbar-nav navbar-right">
  <!-- nav는 실제로 메튜버튼 들이 들어간다. 위의 navbar와 헷갈리면 안 된다.  -->
  <!-- navbar-nav는 실제 메뉴 버튼들이 메뉴 버튼 답게 만들어준다. a태그의 파란색 글씨를 없애거나,  float 속성을 준다 -->
  <!-- navbar-right을 통해 메뉴들을 오른쪽으로 붙인다. -->

        <li><a href="#">방 검색</a></li>
        <li><a href="#">관심목록</a></li>
        <li><a href="#">방 등록</a></li>
        <li><a></a></li>
        <li><a href="#">공인중개사 가입</a></li>
        <li><a href="">회원가입 및 로그인</a></li>
      </ul>
    </div>
  </nav>

  <div class="index-content">
    <div class="jumbotron index-image-container">
  <!-- 점보트론은 중요한 콘텐츠를 보여주기 위해 선택적으로 전체 뷰포트로 확장할 수 있는 가볍고 유연한 콤포넌트이다.-->
  <!-- 단, container 클래스안에 넣으면 점보트론을 최대 너비로 만들 수 없다. -->
      <div class="caption-container">
        <p class="caption-top">850만 명이 선택한 대표 부동산 앱</p>
        <p class="caption-bottom">우리, 살고 싶은 데서 살자</p>
      </div>
    </div>
  </div>


</body>
</html>


```
부트스트랩이 참 신기한 것 같다. 메뉴바 만들다 코드가 한가득 쌓이고 헥헥 거렸는데 코드가 정말 깔끔하고 짧다.<br><br>


다음은 어썸한 SASS 코드이다.
```sass
nav.navbar-no-margin
  margin: 0
/* */
/*네비게이션에서 아래 어색한 마진을 없애기 위해 만들었다. */

.index-content
  .index-image-container
    position: relative
/* 디폴트는 static이다. 속성을 relative로 바꿔줌으로써 위치를 변경할 수 있다. */
    background-image: url(../images/index-bg.jpg)
/* 우리 혜리의 관능적인 모습을 보여주는 다방 사진이다. */
    background-position: 50% bottom
/* 배경이 위치할 곳이다. 첫 번째 인자를 50%로 줌으로써 가운데로 왔다. top과 bottom은 여기서는 같은 결과를 낸다. */
    background-repeat: no-repeat
/* no-repeat으로 주지 않으면 화면이 클 경우 혜리가 여러 번 등장한다. 그것을 막기 위해 반복을 없앤다. */
    background-color: black
/* 반복을 없애고 남은 옆 공간들에 검은색을 줌으로써 마치 검은 배경과 사진이 한 폭의 장면인 것처럼 연출했다. */
    height: 678px


/* 밑의 클래스는 화면의 두 줄을 표현하기 위해 만들었다. */
    .caption-container
/* 먼저 스타일이 다른 두 텍스트를 묶을 하나의 큰 콘테이너를 만든다. */
      position: absolute
/* 포지션을 absolute로 준 것이 의미심장하다. absolute로 속성을 줌으로
  부모클래스를 기준으로 위치를 지정할 수 있고 따라서 크라우저의 크기 변화와
  관계 없이 텍스트가 항상 원하는 위치에 있을 수 있도록 한다. */
      left: 50%
/* 부모의 왼쪽으로부터 50%까지 쭉 온다. 그 결과 불독의 머리 위에 항상 글이 위치한다. */
      top: 160px
/* 160px만큼 값을 줌으로써 글자를 천장에서 내린다. */
      margin-left: -420px
/* 이 값을 줌으로써 50%에서 왼쪽으로 당긴다.  */
      color: white
      text-align: right
/* 크기가 서로 다른 두 문자열이 오른쪽으로 같은 부분에서 끝남을 알 수 있다. 이 속성 때문에 그렇다. */
      .caption-top
        font-size: 22px
        margin-bottom: 0
/* 위에 글씨가 작으므로 22px만큼한 준다. 밑의 마진을 0으로 준 것은 둘의 위아래 간격을 좁히기 위함이다.*/
      .caption-bottom
        font-size: 36px
/* 큰 글씨는 36px을 주었다. */


```
