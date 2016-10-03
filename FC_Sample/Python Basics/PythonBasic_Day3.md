
# __◈ Python__
## Python basics: Day 3
작성 날짜 : 2016-10-02

# 1. *Decorator*

## 1.1 Introduction
파이썬에는 *Decorator*(이하 데코레이터)라는 개념이 있다. 나같은 경우에는 공부할 적에 메소드를 만들 때 객체 안에 `@classmethod`라는 데코레이터를 넣으면 인스턴스 메소드가 아닌 클래스 메소드가 된다고 어렴풋이 알고만 있었고 제대로 알아보지는 못했다. 데코레이터는 글쎄, **함수를 받아서 새로운 함수를 만들어 반환하는 함수**로 정의할 수 있겠다.  자세히 알아보자.

### 1.1.1 함수의 실행시간을 측정하는 함수를 만들자.
> `print`문을 10번 돌린다고 할 때 `for`문을 돌리는 것보다 `print`문을 10번 찍어넣는 게 속도가 빠르다고 한다. 이런 문제들에서 나는 함수의 성능을 측정하고 싶었다고 해보자.

```python
import time
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")

start_time = time.time()
hello("안수찬")
end_time = time.time()
exec_time = end_time - start_time
print("Execute Time: {time}".format(time=exec_time))

>>> 안녕하세요, 저는 안수찬 입니다.
>>> Execute Time: 8.893013000488281e-05
```

> 위와 같이 `hello`라는 함수를 만들고 그 성능을 측정하기 위한 식을 적었다. 매번 이렇게 적을 수는 없으니 새로운 함수를 만들자.


```python
def new_hello():
    start_time = time.time()
    hello()                                       
    end_time = time.time()
    exec_time = end_time - start_time
    print("Execute Time: {time}".format(time=exec_time))

new_hello('박군')

>>> 안녕하세요, 저는 박군 입니다.
>>> Execute Time: 2.5510787963867188e-05
```

> `hello`라는 함수를 포함하는 새로운 함수를 만들었다. 얼핏 보면 그럭저럭 좋아보인다. 그런데, **이런 실행 시간을 측정하는 함수를 원하는 함수들에다 일일이 작성해야 한다면 귀찮기도 하고, 시간자원을 많이 잡아먹는 비효율적인 작업이 될 것이다. 확장성이 떨어지기도 한다.** 편하게 원하는 모든 함수들의 시간을 측정하는 방법은 없을까?

### 1.1.2 함수를 반환하는 함수를 만들자.
> 위의 문제를 해결하는 방법으로 곧바로 들어가기 전에 이런 생각을 해보자. **함수를 반환하는 함수를 만들 수 있을까?**

```python
def get_multiply_by(n):
    def return_function(x):
        return x * n
    return return_function
the_function = get_multiply_by(5) #!!!
print(the_function(10))

>>> 50
```
>위의 함수를 잘 생각해보자. `get_multiply_by` 함수는 'n'을 받는다. 그리고 `return_function`이라는 함수를 반환하는데, 이 함수는 'x'를 받으면 그 수에 'n'을 곱해 반환하는 함수다. <br>
그렇다면, '#!!!'에서 볼 수 있듯이 `the_function`을 마음대로 customizatioe을 할 수 있다. 우리는 이번에는 input에 5배를 해 반환하는 함수를 만들었지만, 원하면 다른 값을 넣을 수도 있다. <br>
즉, 함수(`return_function`)를 만드는 함수`get_multiply)by`를 만든 것이다.

> **그렇다면 여기서 확장하자. `hello`를 받아서 `new_hello`를 만드는 함수를 만들 수 있지 않을까?** 그 함수는 customization하기 쉽겠지. 그것이 데코레이터다.

### 1.1.3 데코레이터 기본 문법
위에서 만든 `hello`, `new_hello`를 데코레이터로 구현해보겠다.

```python
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")

# decorator => 함수를 input 으로 받아서 => 새로운 함수를 만들어서 리턴하자.
# 함수를 받아 새로운 함수를 리턴하는 함수

1. def track_time(func):               
2.    def new_func(*args, **kwargs):
3.        start_time = time.time()
4.        func(*args, **kwargs)
5.        end_time = time.time()
6.        exec_time = end_time - start_time
7.        print("Execute Time: {time}".format(time=exec_time))
8.    return new_func

9. hello = track_time(hello)
hello("안수찬")                 

>>> 안녕하세요, 저는 안수찬 입니다.
>>> Execute Time: 4.6253204345703125e-05
```

> 1. 명심하자. **우리는 확장성을 위해 `new_hello`를 매번 만들지 않고 데코레이터를 만든다.** `track_time`는 데코레이터 함수이다. **인자로 함수를 받는다.**
> 2. 우리가 반환할 함수를 안에서 정의한다. 우리는 확장성을 위해 *pack*한다. 어떤 함수에 재사용될지 모른다. 그렇기 때문에 대비한다.
> 3. 시간 측정을 위한 문장이다.
> 4. **우리는 맨 처음인자로 함수를 받았다.(`func`) 그 함수를 실행하는데 인자로는 아까 *pack*한 인자들을 다시 *unpack*해서 넣는다.**
> 5. 시간 측정을 위한 문장이다.
> 6. 시간 측정을 위한 문장이다.
> 7. 시간 측정을 위한 문장이다.
> 8. 그 함수를 반환함으로써 원 함수가 customization 되었다.
> 9. 원형 `hello` 함수를 새로 만들어 시간측정까지 되는 함수로 탈바꿈되었다. 위와 같이 하면 다른 함수에도 `track_time`을 뒤집어씀으로써 시간을 언제든지 측정할 수 있따.


### 1.1.4. 데코레이터 기호
위에서 우리는 `hello = track_time(hello)` 라는 식으로 함수를 뒤집어 썼는데 파이썬에서는 이것을 '@'기호로 지원하고 있다.

```python

@track_time  # <- 데코레이터 기호!
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")
```

> 위와 같이 `hello` 함수 위에 `@track_time`이라고 적으면 **`hello`함수를 인자로 받아서 `track_time` 함수가 데코레이트(장식)하여 새로운 함수가 반환된다.** 이름은 `hello` 그대로이지만 데코레이터가 있을 때, 없을 때 결과가 완전 다르다. `@track_time`이라는 데코레이터와 함께 우리는 어떤 함수에든 시간을 쉽게 측정할 수 있을 것이다.

### 1.1.5 데코레이터 중첩
위의 함수에서는 하나의 함수에 데코레이터가 하나가 붙었다. 그런데 데코레이터는 많이 붙을 수도 있다. 이렇게 해보자.

```python
def start_func(func):
    print("start_func decorator 적용 시점")
    def wrapper(*args, **kwargs):
        print("==== 함수를 시작합니다 ====")
        return func(*args, **kwargs)
    return wrapper

def finish_func(func):
    print("finish_func decorator 적용 시점!")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("==== 함수를 종료합니다 ====")
        return result
    return wrapper
```
> 시간을 측정하는 데코레이터뿐 아니라, 함수의 시작과 끝을 알려주는 데코레이터 함수도 동시에 만들었다.

```
@track_time
@finish_func
@start_func
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")

hello("안수찬")

>>> ==== 함수를 시작합니다 ====
>>> 안녕하세요, 저는 안수찬 입니다.
>>> ==== 함수를 종료합니다 ====
>>> Execute Time: 0.0005345344543457031
```

> 원형 함수에 시간측정은 물론, 시작과 끝까지 선언되는 데코레이터가 완성되었다.

## 1.2. 데코레이터의 활용
위에서 우리는 데코레이터의 기본개념을 배웠고 실제로 시간측정이라는 의미 있을 수 있는 곳에 활용해봤다. 또 다른 어썸한 데코레이터의 예가 있을까? 살펴보자.

### 1.2.1. Fibonacci 

#### 1.2.1.1. Fibonacci 수열 소개.
너무나 유명한 수열이다. 모두가 알다시피 Fibonacci 수열은
> 0  |   1  |   1  |   2 |   3 |   5 |  8 |  13 |  21 |  34 |  55 | 89

처럼 뒤의 두 수를 더한 값이 그 다음 값이 뒤는 수열이다. 이 식을 쉽게 파이썬으로 구현해보면 다음과 같다.

```python
def fibonacci(n):
	return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)

>>> 55
```
식 자체는 매우 간단한데 이런 기본적인 Fibonacci의 활용에는 매우 치명적인 약점이 있다. **n이 2 이상일 때는 피보나치 함수가 둘로 분기해서, n이 커지면 커질수록 계산 자체가 매우 복잡해진다는 것이다.** n이 100만 되어도 fibonacci 계산이 몇 번이 중복되는지 모른다. 그래서 알고리즘 문제식에서 이 문제를 위와 같이 풀면 시간에러가 나는 경우가 많은 것이다. 이 문제를 데코레이터로 활용해보자.

#### 1.2.1.2. 동적 계획법(*Dynamic programming*)
> 위 문제를 우리는 동적 계획법, 또는 기억하며 풀기 기법으로 해결할 것이다. 동적계획법이란 컴퓨터공학, 수학 등에서 **복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법을 말한다.** <br>
> 피보나치 수열에서 우리는 n이 커질 때마다 그보다 작은 피보나치를 계속 계산해주어야 한다. 예를 들면, n이 5라면 아래처럼 같은 계산을 수없이 반복해야 한다. 
```
f(5) = f(4) + f(3)
      = (f(3) + f(2)) + (f(2) + f(1)) + f(3)
      = (f(3) + f(2)) + (f(2) + f(1)) + (f(2)+f(1))
 ``` 

> 저 계산을 어떻게 줄일까? **n이 3일 때를 처음 구하고, 그 값을 저장한다면(기억한다면) 다음 3의 값이 필요할 때 계산 중복을 피할 수 있지 않을까?**
> 이 생각을 실현할 것이며 이번 피보나치 수열에서 우리가 사용할 방법은 [*memoization*](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98)기법으로 *memoization*은 동적 계획법의 핵심이 되는 기법이다.

> 즉, 피보나치 수열의 결과를 cache에 저장할 것이며, 그 값들을 _indexing_하여 계산을 줄일 것이다.

```python
def cache_memoization(func):
    __cache = {}
    def wrapper(*args):
        if args in __cache:
            return __cache[args]
        else:
            result = func(*args)
            __cache.update({args:result})
            return result
    return wrapper
        
@cache_memoization
def fibo(n):
    return n if n < 2 else fibo(n-1) + fibo(n-2)

fibo(100)

>>> 354224848179261915075
```

> 위 방법의 핵심은 `__cache`라는 캐시 변수를 만들어놓고 받은 인자에 해당하는 값이 있으면 반환하면 없을 때 계산을 수행하는 방법이다. 이렇게 하면 한 번 계산해본 값은 `__cache`에 저장되어 다음 식에서 중복 계산할 필요없이 바로 가져다 쓰며 아직 검색을 해보지 않은 경우 계산을 한 뒤 값을 `__cache`에 저장하면 된다. <br>
> 그 결과 100에 달하는 숫자를 넣어도 계산이 된다... ~~엄청 크다..~~


> 저 `cache_memoization`함수를 내가 좋아하는 안수찬 샘은 한 줄로 함드신다. 겁먹지 말고 저렇게도 할 수 있다 정도로만 이해하자.


```python
def cache_memoization(func):
    __cache = {}
    return lambda *arg: __cache[arg] if arg in __cache else __cache.update({arg:func(*arg)}) or __cache[arg]


# 설명이 필요하면 박성환을 찾아오자
```


# 2. 객체 지향 프로그래밍(Object Oriented Programming)
프로그래밍을 하는 다양한 패러다임이 존재한다. 우리가 기본적으로 사용한 방법은 아마 절차지향 프로그래밍(Procedure Oriented Programming)일 것이다.
순서대로 코딩을 짜놓고 그 '절차', '흐름'에 프로그램의 방향을 정하는 패러다임이다. C언어 등이 해당된다고 할 수 있다.<BR>
아마 객체지향, 객체라는 말을 매우 많이 들어봤을 텐데 파이썬은 *lambda* 와 같이 함수지향 프로그래밍도 지원하지만 자바처럼 객체지향 프로그램도 지원한다.
객체 지향이 도대체 뭘까? 내 나름대로의 설명을 해본다.

## 2.1. Introduction to OOP
### 2.1.1. 객체...
> 이 지구에서 가장 영향력 있는 존재를 찾으라면 인간이 될 것이다. 인간은 지구에 적응하기를 넘어서 지배하기에 이르렀고 인간 개개인은 자신의 행동의 '주체'로서 행동한다.
> 그리고 우리를 둘러싼 수많은 객체들이 있다. 내 곁에만 해도 마우스, 노트북, 커피잔, 내 가방.. 이들은 세상을 이루는 객체이다.
> 기존 절차지향은 프로그램 안에서 코드가 순서대로 실행되는 단순한 흐름의 패러다임이었다.<br>
> 그런데 자바 등이 원하는 방향은 세상은 너무나 복잡한 객체들의 상호관계로 이루어져 있고, 그들을 일정한 객체의 묶음으로 표현하면
> 복잡한 세상을 잘 표현할 수 있지 않을까라고 생각했고, 제임스 고슬링은 자바에서 객체지향 프로그래밍을 떠올렸다.<br>
> **객체 지향은 실제 객체들을 일반적인 특징으로 묶어 클래스(*class*)라고 칭하고 그들의 실제적인 예를 인스턴스(*instance*)라고 일컫는다.**
> **이 속에서 우리를 둘러싼 사물, 물건들은 더 이상 수동적인 존재가 아니며 각자의 특성(attribute)과 행동(behavior)을 갖는 고유한 객체가 된다.**

> 개인적으로 좋아하는 시가 하나 있다. 

```
오렌지
                  신동엽

오렌지에 아무도 손을 댈 순 없다.
오렌지는 여기 있는 이대로의 오렌지다.
더도 덜도 아닌 오렌지다.
내가 보는 오렌지가 나를 보고 있다.

마음만 낸다면 나도
오렌지의 포들한 껍질을 벗길 수 있다.
마땅히 그런 오렌지
만이 문제가 된다.

마음만 낸다면 나도
오렌지의 찹잘한 속살을 깔 수 있다.
마땅히 그런 오렌지
만이 문제가 된다.

그러나 오렌지에 아무도 손을 댈 순 없다.
대는 순간
오렌지는 이미 오렌지가 아니고 만다.
내가 보는 오렌지가 나를 보고 있다.

나는 지금 위험한 상태다.
오렌지도 마찬가지 위험한 상태다.
시간이 똘똘
배암의 또아리를 틀고 있다.

그러나 다음 순간,
오렌지의 포들한 껍질에
한없이 어진 그림자가 비치고 있다.
누구인지 잘은 몰라도.

```

> **내가 보는 오렌지가 나를 보고 있다.** 오렌지는 단순히 내가 먹는 물건 이상을 넘어서 자신의 행동을 가지고 있는 객체가 되었다.
> 난 이 시에서 객체지향을 보았다.


