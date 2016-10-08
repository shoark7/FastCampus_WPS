# <center>pyenv, django 프로젝트 환경설정하기 </center>

#### <p style='text-align:right;'>2016/10/08 </p>
#### <p style='text-align:right;'>박성환		 </p>

&nbsp;&nbsp;&nbsp;앞으로 우리는 수많은 프로젝트에 직면할 것이다. 그리고 프로젝트마다 서로 다른 환경, 버젼을 요구할 것이고, 따라서 기본이 되는 환경설정은 매우 중요하다.<br>
&nbsp;&nbsp;&nbsp;그래서 주말 동안 한영샘이 내주신 과제는 장고, 파이썬 프로젝트의 pyenv, virtualenv 설정, 장고 설치, 파이참에 인터프리터 세팅까지 프로젝트의 '기본' 세팅을 처음부터 다시 해보는 것이다.<br>
진행할 과정은 다음과 같다.

> 1. pyenv 전체삭제
> 2. pyenv 재설치
> 3. pyenv 에 파이썬 3.4.3설치
> 4. 가상환경 생성
> 5. pip로 장고 설치
> 6. 장고 프로젝트 생성
> 7. 파이참으로 프로젝트폴더 열기
> 8. 해당 프로젝트에 가상환경 인터프리터 세팅
하나씩 진행해 나가자.<br> <br><br>


## 1. pyenv 전체 삭제.
[pyenv][pyenv]는 파이썬의 버전을 자유롭게 변경할 수 있는 도구이다. 전에 안수찬 샘 강의에서 설치했기 때문에 과제를 위해 먼저 삭제한다.<br><br>

과정은 어렵지 않다. `.pyenv` 폴더를 완전히 날려 버린다. ~~슬프다..~~<br>
터미널에 다음과 같이 입력한다.

`rm -rf ~/.pyenv`

`-r` 옵션은 'recursive'의 약자로 안의 파일, 폴더까지 연쇄적으로 삭제하며,<br>
`-f` 옵션은 'force'의 약자로 가차없이(경고 등 없이) 다 날려버린다는 강력한 의미다.

```linux
➜  ~ :  cd ~/.pyenv
cd: 그런 파일이나 디렉터리가 없습니다: /home/sunghwanpark/.pyenv
```

<br>
완전히 삭제되었다.
<br><br><br>

## 2. pyenv 재설치
먼저 pyenv의 [github][pyenv]에 들어간다. 그러나 이 repository에는 README.md에는 pyenv의 동작원리 등을 길게 설명하고 있고 설치에 대한 이야기는 없다.
<br> 대신 중반 이후에 설치를 위해서는 [pyenv-installer][pyenv-installer]라는 다른 repository를 방문하라고 안내하고 있다.<br><br>

pyenv-installer repoitory에는 바로 운영체제별 설치에 대한 안내를 하고 있다.
<br>다음과 같이 입력한다.

`curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`
<br>
금방 설치된다. 그리고 다음 문장을 `.bashrc`에 추가한다.

```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
"내 컴퓨터 기준으로" 이렇게 입력한 뒤 `pyenv`를 쓰려고 하면 잘 안 될 것이다. 왜냐하면 dependency를 설치해야 하기 때문이다. pyenv가 작동하기 위해 의존하는 것들을 말한다.<br>
pyenv repository로 다시 돌아온 후 wiki를 클릭한 뒤 오른편에 [Common build problems][build-problem]이라고 적힌 부분이 있다. pyenv가 작동하기 않을 때 대표적인 경우들을 모아놓았다.<br>
바로 보이는 **Requirements** 섹션에
ubutnu 용으로 제시된 코드를 실행하자.

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```
<br>
수찬 샘이 모든 프로그램, 환경설정 설치 과정은 이렇게 1. 깃허브 등에서 소스 찾아서 설치하고, 
2. 안 되면 dependency 찾아보고 의 연속이라고 하셨는데 그런 면에서 한 번 더 해보는 것이 의미가 있는 것 같다.<br><br>

'pyenv'라고 터미널에 입력했을 때 다음과 같이 나오면 정상이다.
```
pyenv 1.0.2
Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   commands    List all available pyenv commands
   local       Set or show the local application-specific Python version
   global      Set or show the global Python version
   shell       Set or show the shell-specific Python version
   install     Install a Python version using python-build
   uninstall   Uninstall a specific Python version
   rehash      Rehash pyenv shims (run this after installing executables)
   version     Show the current Python version and its origin
   versions    List all Python versions available to pyenv
   which       Display the full path to an executable
   whence      List all Python versions that contain the given executable

See `pyenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/yyuu/pyenv#readme
```
<br><br><br>





## 3. pyenv에 파이썬 3.4.3 설치
터미널에 `pyenv versions`라고 입력하면 'system'만 나올 것이다. 우분투에 기본적으로 설치된 파이썬 버전이다.<br>
이제 pyenv에 다양한 파이썬 버전을 설치하자. <br>
'pyenv install _버전명_'을 통해 원하는 버전을 설치할 수 있다. 난 일단 3.5.2 버전을 설치한다.

`pyenv install 3.4.3`
시간이 조금 걸리면 설치가 완료된다. `pyenv versions`를 다시 입력해보면 원하는 버전이 설치되었음을 알 수 있다.
<br><br><br>

## 4. 가상환경 생성
pyenv를 통해 버젼의 구속에서 벗어날 수 있었다. 그러나 여기서 끝나지 않는다.<br>
장고 프로젝트를 여럿 하는데 프로젝트마다 **사용하는 장고의 버전이 다를 수도 있을 것이다.** 즉 프로젝트마다 라이브러리의 구속도 해결해야 한다.<br>
가상환경은 'virtualenv'라는 이름으로 만들 수 있는데<br>
**pyenv가 파이썬의 버젼을 자유롭게 해준다면, virtualenv는 프로젝트별 라이브러리의 버전을 자유롭게 해준다.**<br><br>

그리고 pyenv가 virtualenv 환경도 같이 지원한다. 'homework'라는 프로젝트에서 사용할 virtualenv 환경을 만든다면 다음과 같이 입력한다.<br>
`pyenv virtualenv _파이썬버전_ homework`
이 뜻은 **'해당 파이썬 버전을 지원하는 'homework'라는 가상환경을 만든다'**이다. 다시 'pyenv versions'를 입력하면 생성결과를 알 수 있다.

```
➜  ~ pyenv versions
* system (set by /home/sunghwanpark/.pyenv/version)
  3.5.2
  3.5.2/envs/django-project
  django-project
```
그리고 <br>
`pyenv activate django-project` 라고 입력해 해당 가상환경에서 작업할 수 있다.
`pyenv deactivate`는 활성화된 가상환경을 해제할 때 사용한다.
<br><br><br>

## 5. pip로 장고 설치
`pip`은 'Python Installs Python', 'Python Install Program' 등의 약자로, 파이썬 패키지를 다운 받을 수 있는 프로그램이다.,<br><br>

먼저 `pip list`라고 입력해보자. 기본적으로 장고가 설치되어 있지 않을 것이다.<br><br>

패키지 설치는 `pip install _패키지명_`처럼 입력해서 패키지를 다운할 수 있다. 원하는 가상환경 위에서 django를 설치한다.<br>
`pip install django`<br><br>

다시 한 번 목록을 살펴보면 장고가 설치되었음을 알 수 있다.
<br><br><br>

## 6. 장고 프로젝트 생성
이전까지가 프로젝트를 위한 세팅이었다면 지금부터는 장고 자체의 세팅이다.<br>
장고가 설치된 가상환경 위 그리고 프로젝트가 생성되길 원하는 경로에서 다음과 같이 입력한다.<br>
`django-admin startproject _프로젝트명_`<br>

이후 app을 만드는 등의 기술적인 부분은 과제의 범위를 넘어서 설명하지 않는다.


<br><br><br>
## 7. 파이참으로 프로젝트폴더 열기
WPS에서는 파이참(PyCharm)으로 장고를 관리한다. 파이참에서 우리의 프로젝트를 오픈하자.<br>

`File > Open > _원하는 프로젝트_`
<br><br><br>



## 8. 해당 프로젝트에 가상환경 인터프리터 세팅
우리는 프로젝트가 아까 만든 가상환경 위에서 동작하기를 바란다. 근데 별도로 지정해주지 않으면 파이참은 기본 설치된 파이썬 버전으로 코드를 실행할 것이다.<br>
그래서 프로젝트에 맞는 가상환경 인터프리터를 세팅하자.<br>

`File > Settings > Project: *프로젝트명* > Project Interpreter`<br>
에서 우리가 원하는 가상환경을 선택하고 `OK`를 누른다.<br><br>





[pyenv]:https://github.com/yyuu/pyenv
[pyenv-installer]:https://github.com/yyuu/pyenv-installer
[build-problem]:https://github.com/yyuu/pyenv/wiki/Common-build-problems
