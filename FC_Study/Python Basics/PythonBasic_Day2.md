
------------------- 2일차 -------------------------------------------------------

# ◈ Python
## Python basics: Day 2
작성 날짜 : 2016-09-25
## 0. 파이썬에서의 삼항연산자.
자바 등에서 삼항 연산자(ternary operator)을 본 적이 있을 것이다.  `a ? a>b : b` ~~이거 맞나?~~

저 것의 뜻은 a가 b보다 크면 a를 쓰고, 조건이 충족되지 않으면 b를 쓴다는 것이다. if, else를 사용해서 할 수 있는 식인데 워낙 많이 사용되므로 한 줄로 사용가능하도록 만들어 놓은 것이다.

이것이 파이썬에도 구현되어 있다.
```python
k = 3
print(k) if k < 4 else print('hi')

l = 'my name is park'
print(l) if len(l) <= 10 else print('too long')

>>> 3
>>> too long

"""
첫 번째 식은 k가 4보다 작아서 조건을 만족함으로 맨 3을 출력하였고,
두 번째는 l의 길이가 10을 훌쩍 넘기기 때문에 조건을 만족시키지 않았고, 따라서
'too long'을 출력햇다.
위와 같이 간단한 조건식은 삼항연산자를 통해 계산할 수 있다.
"""
```

## 1. 전 날 배운 내용을 활용해보자.

### 1.1. n이라는 숫자를 받아서 n 개의 짝수 리스트를 만드는(return) 함수
example :  100 => [0, ..., 198]
```python
result = []
n = 100
for i in range(n):
    element = i * 2
    result.append(element)
len(result) == n

# --- 이것을 함수로 만들자.

def get_even_list(n): 
    result = []
    for i in range(n):
        element = i * 2
        result.append(element)
    return result
```

### 1.2. n 이라는 숫자를 input 으로 받아서, 0부터 n 보다 작은 짝수 리스트를 만드는 함수 
 100 => [0, ..., 98]

```python
result = []
n = 100          # result = [0, ..., 98] (len(result) == 50)

for i in range(n):
    if i%2 == 0: # i를 2로 나눈 나머지가 0이라면, 즉 짝수라면!
        result.append(i)

# --- 이것을 함수를 사용해서도 만들어보자.

def is_even(n):
    return i%2 == 0
    # even => True
    # odd => False

for i in range(n):
    if is_even(i):
        result.append(i)
# 사용자가 만든 함수를 사용해 좀 더 간단하게 구했다.
```

### 1.3. FizzBuzz
이 문제는 꽤나 유명하다고 한다. 369 게임과도 비슷한데, 
기본적으로는 1부터 100까지 숫자가 3의 배수이면 'Fizz'를 출력하고, 5의 배수일 땐 'Buzz'를 출력하며 15의 배수일 땐 'FizzBuzz'를 출력하는 것이다. 아무것도 해당 안되면 빈 값을 출력한다. 해보자.
```
# list #1: ["", "", "fast", "", "", "fast", ]
# list #2: ["", "", "", "", "campus", ]

# -------------------------------------------

# list => ["", "", "fast", "", "campus", "fast", ... "fastcampus", ...]
```
실제로 구현하자.

```python
result = []
n = 100

for i in range(n):
    element = ("fast" if (i+1)%3==0 else "")      # 1.
               + ("campus" if (i+1)%5==0 else "") # 2.
    result.append(element)
```
여기서는 조건식이 두 번 사용된다. 먼저 1. 첫 번째인 숫자가 3의 배수인지 검증하고 맞으면 'fast'을 붙인다. 2. 두 번째는 만약 5의 배수라면 'campus'를 붙인다. 15의 배수라면, 그러니까 3으로 나눠지기도 하고, 5로 나눠지기도 한다면 'fastcampus'처럼 두 문자열이 붙을 것이다. 그 `element`를 `result`에 붙인다. 그 짓을 100번 한다. 처음에 하기에 무난한 식이라고 할 수 있을 것이다.

### 1.4. FizzBuzz를 확장하자.
위의 FizzBuzz도 무난하다. 그러나 좋은 식이란 확장가능한 식이다. 위의 예를 함수화해서 더 편하게 사용가능하도록 해보자.

```python
def get_list(n, rule1, rule2):
    result = []
    for i in range(n):
        element = ""          # 1.
# --------------------------------------
        for rule in [rule1, rule2]:  
            div, text = rule
            element += text if (i+1)%div == 0 else "" # 2.
# --------------------------------------
        result.append(element)
    return result

print(def get_list(100, (3, 'Fizz', 'Buzz'))

''
''
'Fizz'
''
'Buzz'
....
```
&nbsp;&nbsp;`get_list`라는 함수로 만들어봤다. `n`은 몇까지 함수로 적용할 것인지 정할 수 있다. `rule1`, `rule2`는 `(3, 'Fizz')`, `(5, 'Buzz')`처럼 몇 으로 나누고 어떤 text를 붙일지 정할 수 있다. 이렇게 함으로써 꼭 3, 5로 나누는 것이 아닌 7, 10 등 다양하게 적용해볼 수 있다. 

&nbsp;&nbsp; rule들을 `for`문 돌리면서 i라는 숫자가 각각 숫자로 나눠떨어지는지 확인한다. 각 rule들은 `(3, 'Fizz')`처럼 인자가 두 개인 튜플로 들어있다. 여기에 `div, text = rule`처럼 적으면 `div=3; text='Fizz'`처럼 적용이 된다. `rule[0] rule[1]` 처럼 사용한다면 가독성이 꽤나 침해당할 것이다. 위처럼 쓰면서 코드의 질을 높일 수 있다.삼항연산자를 사용해 각각을 나눠 text들을 element에 붙인다. 

&nbsp;&nbsp; 그 결과를 `result`에 붙인다. 그리고 `result`를 반환한다.



### 1.5. 입력받은 숫자 n이 정수인지 검증해보자
정수 n이 소수인지 확인하는 방법은 매우 많다. 그렇지만 가장 무난하고 확실한 방법인 자신보다 작은 정수로 나눠보는 방법을 사용해보자.

```python
def is_prime(n):
    """n 이 소수인지, 아닌지 판별하는 함수"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(4))
print(is_prime(100))

>>> True
>>> False
>>> False
```
&nbsp;&nbsp;소수의 정의는 1과 자기 자신만을 약수로 갖는 정수이다. 그렇다면 그 이외의 값으로 나눠떨어지는 경우가 한 번이라고 있다면 그 정수는 소수가 아니라는 것이 된다. `for`문으로 '2'부터 'n-1'까지 나눠보면서 나눠떨어진다면 바로 `False`를 반환한다. 만약 그 삼엄한 `for`테스트를 모두 통과하면 그 수는 소수라는 것이 증명된 것으로 True를 반환하게 된다.<br/>
```python
n = 100
result = []

for i in range(2, n):
    if is_prime(i):
        result.append(i)
result
```
&nbsp;&nbsp; 이 식은 2부터 100까지 정수인지 확인하고, 정수일 경우에만
결과 리스트에 값을 집어넣는 식이다. 용자들은 이렇게 해서 10000보다 작은 소수들을  출력해보는 건 어떨까? ~~생각보다 쾌감이 있다.~~


### 1.6. 입력 받은 숫자들의 합을 출력하는 함수를 만들자
```python
def get_sum(elements):
    result = 0
    # -------------------------------------
    for element in elements:
        result += element
    return result
```
&nbsp;&nbsp;기본적으로는 위와 같이 만들 수 있을 것이다. 기본 값을 0으로 두고 리스트 등을 `for`문을 돌면서 모두 더한다. 그 결과 `result`를 출력하면 전체 합이 나온다.


### 1.7. 입력 받은 숫자들 중 최대값을 출력하는 함수를 만들자.
```python
def get_max(elements):
    result = elements[0]   # 초기값!
    for element in elements:
        if element > result:
            result = element
    return result
```
&nbsp;&nbsp;위와 비슷하지만 조금 다른다. 여기서는 초기값을 '0'으로 잡으면 안 될 것이다. **모든 원소가 음수일 경우 최대값이 0으로 출력될 것이기 때문이다.** 따라서 첫 번째 원소를 주어진 리스트의 기본값으로 잡는다. `for`문을 돌면서 `result`를 보다 큰 값으로 계속 덧씌운다. 마지막에 나오는 값을 결국 리스트의 최대값이 된다.



## 2. _lambda_와 _lambda operator_를 알아보자.
&nbsp;&nbsp;안수찬 선생님은 함수형 프로그래밍을 참 좋아하시는 것 같다. 파이썬에서도 함수형 프로그래밍 기능을 일부 지원하는데 이는 _lambda_와, _lambda_와 같이 붙어다니는 _lambda operator_로 만들 수 있다.

### 2.1. _lambda_
&nbsp;&nbsp; _lambda_는 익명 함수, 무기명 함수 등으로 불린다. 매우 간단한 함수를 만들 경우 `def` 키워드 대신 `lambda` 키워드를 사용한다면 훨씬 더 짧고 간단하게 만들 수 있다. 예를 들어보자.
```python
# 숫자를 받아서 2배해 반환하는 함수를 만들자.
def double_maker_def(n):
    return n * 2

# 위처럼 만들 수도 있다. lambda를 써보면
double_maker_lambda = lambda x : x * 2

# 람다를 해석해보자. 람다 함수를 정의할 땐 lambda 키워드를 앞에 놓고, 받는 인자를 'x' 처럼 값을 넣는다. ':' 뒤에 오는 내용은 반환값이 된다. ':'를 일반 함수의 'return'과 비교하면 좋을 것 같다.

```

### 2.1. _lambda operator_
&nbsp;&nbsp; 많은 경우 람다는 스스로만 쓰지 않는다. 보통 람다는 `map`, `filter`, `reduce`라는 함수들과 많이 사용된다.  `map`, `filter`는 빌트인 함수이고, `reduce`는 `functools`라는 모듈을 `import` 한 후 쓸 수 있다. 

하나씩 살펴보자.

#### 2.1.1. map
&nbsp;&nbsp; 위 세 함수의 공통점은 받는 인자의 순서가 동일하다는 것이다.

> **`map( function , iterable )`**
> 첫 번째 인자는 함수다. 어떤 함수를 쓸지 명시한다.
> 람다함수는 많은 경우 한 줄로 표현하기 때문에 여기에 람다를 쓰는 것이다.

> 두 번째 인자는 _iterable_이다. `for`문을 쓰듯이 모든 원소를 한 번씩 반복하면서 함수를 적용할 수 있다.

**map**의 역할은 **리스트 내의 원소 각각에 함수를 적용한 뒤 적용된 _iterable_를 반환하는 것**이다. 쉬운 예를 보자.

```python
k = [1,2,3,4,5,6,7,8,9,10]
k = list(map(lambda x: x * 2, k))
              # 1.            # 2.
print(k)

>>> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
위를 잘 해석해보자. 원 리스트 `k`는 1부터 10까지 정수를 포함하고 있다.

 map의 첫 번째 인자는 람다식을 넣는다 그 내용은 받은 값 `x`를 두 배로 만들어 반환한다는 것이다.(':'이 `return`과 대응된다.) 

두 번째 인자는 리스트 `k`이다. 

**`map`을 통해서 리스트 `k`안에 있는 모든 숫자에 람다식이 적용된다. 람다식은 값을 두 배로 만들어 반환하는 함수이고, `map`의 결과물은 모든 원소가 두 배로 적용된 _iterable_이다.** 그 값을 `list`로 리스트로 다시 바꿔서 `k`에 대입하면 원 리스트에서 모든 원소가 두 배로 된 결과가 나왔다.

`map`의 느낌을 조금 알겠는가? 나머지도 알아보자.


#### 2.1.2. filter
> **`filter( function , iterable )`**

들어가는 인자는 세 함수 모두 동일하다. `filter`는 `map`과 큰 차이점을 가지고 있는데,

`map`이 두 번째 인자의 모든 원소에 함수를 적용해서 모두 반환한다면(결과와 원 리스트의 개수가 동일하다.), **`filter`는 두 번째 인자의 원소들에 함수를 적용해서 조건을 충족하는 원소들만 추출해서 새로운 `filter`객체를 만든다. **예시로 확인하자.

```python
k = [1,2,3,4,5,6,7,8,9,10,]
k_map = list(map(lambda x : x%2 == 0, k))
k_filter = list(filter(lambda x: x%2 == 0, k))

print(k_map)
print(k_filter)

>>> [False, True, False, True, False, True, False, True, False, True]
>>> [2, 4, 6, 8, 10]
```
두 식에서 람다는 동일하다. 받은 값이 짝수면 `True`, 홀수면 `False`를 반환하는 함수이다. `map`에서는 `k`에 람다를 적용해서 각 원소가 `True`인지 `False`인지를 확인해서 모든 결과를 리스트로 반환한다.

**`Filter`는 반대로 `k`에서 람다 조건을 만족하는(즉 결과가 `True`인) 원소들만을 추려서 결과를 반환한다.**

`map`, `filter`의 차이가 이해되는가? 마지막으로 `reduce`를 알아보자.


#### 2.1.3. reduce
##### 2.1.3.1. reduce
`reduce`는 다른 두 함수와 달리 파이썬에서 기본 지원하는 빌트인 함수가 아니므로, `functools`라는 모듈을 `import`해야 한다. 

바로 예를 보자.
```python
from functools import reduce                # 1.
k = [1,2,3,4,5,]                            # 2.
sum_result = reduce(lambda x, y: x+y, k)    # 3.
print(sum_result)

>>> 15
```

'1. `functools` 모듈의 `reduce`함수를 `import`한다.
'2. `k`는 1부터 10까지 정수를 가지고 있는 리스트다.

'3. 여기가 핵심이다.
> reduce의 lambda는 무조건 인자 두 개를 가진다. 여기서는 편의상 `x`, `y`라고 했다.

> 함수로 반환되는 결과물은 다음 `x`으로 저장된다. 그리고는 `k`의 다음 원소와 람다식을 진행한다. 이것을 끝까지 진행한다.

> 그러니까, 맨 처음 람다가 한 번 돌면, `x`에 1, `y`에 2가 들어간다. 람다의 내용은 둘을 더하는 것이므로 결과물 3이 x에 다시 적용된다. 그 다음 반복에서는 3의 값인 `x`에,  1,2, 다음값인 3이 `y`로 된다. 그 둘의 합인 6이 다시 `x`에 적용된다. 다음 람다에선 `x`에 6이 들어가고, 3 다음 값인 4가 `y`에 적용된다.

> 위를 다음과 같이 적을 수도 있을 것이다.
> reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
  =   ((((1+2)+3)+4)+5)

>  이 식을 통해 리스트 내의 모든 원소를 더했다. 아까 구한 `get_sum` 함수를 한 줄로 만들어낸 것이다. 


##### 2.1.3.2. reduce응용하기
```python
rooms = [
    {"rent": 50, "deposit": 1000},
    {"rent": 55, "deposit": 2000},
    {"rent": 60, "deposit": 6000},
]
``` 
당신은 학교 근처에서 자취를 하려고 한다. 매물을 검색하고 결과를 다음과 같이 딕셔너리의 리스트로 저장했다고 가정하자. `rent`는 월세이고 `deposit`은 보증금이다.

여기서 가지고 있는 `rooms`에서 월세의 평균을 `reduce`로 구해보자.
```python
from functools import reduce
reduce(lambda x, y: {'rent':x['rent'] + y['rent']}, rooms)

print(reduce(lambda x, y: {'rent':x['rent'] + y['rent']}, rooms)['rent'] / len(rooms))

>>> 55.0
```
위 식을 잘 뜯어보자.
```python
reduce(lambda x, y: {'rent':x['rent'] + y['rent']}, rooms)
```
`rooms`는 `rent`, `deposit`라는 key와 그에 해당하는 값을 갖는 딕셔너리가 들어 있는 리스트다. 그래서 `reduce`의 두 번째 인자에 `rooms`를 넣으면 각각의 반복에서는 `{'rent':200, 'deposit':100}`과 같은 딕셔너리가 사용될 것이다.

**그렇다면 `x`, `y`는 모두 딕셔너리다.** 한 번의 람다에서 반환되는 값은 당연히 두 딕셔너리의 월세값을 더한 값을 `value`로, `key`를 `rent`로 하는 딕셔너리다. 이 값이 `x`로 들어가고, `y`에는 다음 딕셔너리가 온다. 이렇게 함으로써 `x`, `y` 모두에서 `rent`키의 값을 찾을 수 있는 것이다.(그러니까 _IndexError_없이 말이다.) **핵심은 반환값이 단순히  `x['rent'] + y['rent']`이 아니라는 것이 중요하다.** 이렇게 하면 반드시 오류가 난다. 그 이유를 아는 것만으로 `reduce`의 기본 개념을 이해한 것이다.

```python
print(reduce(lambda x, y: {'rent':x['rent'] + y['rent']}, rooms)['rent'] / len(rooms))

>>> 55.0
```
아까 본 예의 최종 결과물은 `{'rent':165}`가 될 것이다.  결과물에 `['rent']`로 `value` 값을 구하면서 165만 뽑아올 수 있다. 그리고 그 값을 `len(rooms)`으로 나눠서 평균 55.0을 구했다.




## 3. _list comprehension_을 알아보자.
2번에서 우리는 함수형 프로그래밍의 기능인 _lambda_와 _lambda operator_를 알아보았다. 파이썬에서는 추가로 _list comprehension_으로 같은 결과물을 만들어 낼 수 있다. 백문이 불여일견. 일단 보자.

```python
k = [1,2,3,4,5,6,7,8,9,10,]
double_k = [i *2 for i in k]

print(double_k)

>>> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
리스트 컴프리헨션은 `[]` 안에 작성된다. 그 안에 `for i in k` 처럼 일반적인 `for`문을 적고, 그 앞에 각각의 `i`로 할 일을 적는다. 위의 예에선 i를 두 배로 만들게 된다. 리스트 컴프리헨션의 결과물은 무조건 리스트가 된다. 다른 예를 볼까?


```python
k = [1,2,3,4,5,6,7,8,9,10,]
new_k = [i ** 2 for i in k if i % 3== 0]

print(new_k)
print([i ** 2 for i in k if i % 3== 0 if %2 == 0])

>>> [9, 36, 81]
>>> [36]
```
다음 식은 `i`가 3으로 나눠떨어지면 그 수를 제곱하고, 아니면 생략하는 식이다. `if`문을 `for`문 뒤에 적었다. 이를 통해 `i`가 3으로 나눠떨어질 때만 그 수를 제곱해 리스트를 만드는 식이 가능해졌다. 신기하게도 저 식의 뒤에는 `else`가 적용되지 않는다. _SyntaxErorr_가 발생한다. 그리고 `if` 문을 여러 개 적음으로써 조건을 `and`으로 검사할 수도 있다. `or`을 `if` 안에 넣어보았으나 불가능해보인다.



## 4. _args_와 _kwargs_에 대해 알아보자.
박성환이라는 사람을 오랫동안 괴롭힌 문제가 있다. 다음을 보자.
```python
print('max(1,2,3) is',str(max(1,2,3)))
print('max([1,2,3]) is',str(max([1,2,3])))

>>> max(1,2,3) is 3
>>> max([1,2,3]) is 3
```
받은 값들의 최대값을 구하는 `max`함수는 받은 값이 리스트이든, 값 여러 개이든 문제없이 최대값을 구해준다. 

```python
print('sum([1,2,3]) is',str(sum([1,2,3])))
print('sum(1,2,3) is',str(sum(1,2,3)))

>>> TypeError: sum expected at most 2 arguments, got 3
```
이와는 대조적으로 받은 인풋의 합을 구해주는 `sum` 함수는 `sum(1,2,3)`처럼 인자를 여러 개 넣으면 `TypeError`를 반환한다. 같은 빌트인 함수인데 일관성이 결여된 것이 아닐까? 일단 이 문제에 대한 토론은 나중에 하자. 이런 함수의 인자와 관련된 것이 *args와 **kwargs이다. 하나씩 알아보자.


### 4.1. *args
우리는 함수를 호출할 때, 많은 경우 인자를 입력한다.
```python
k = int('3')
argl = print('a', 'b', 'c', ' \ ', '', fp, True)
kwargl = print('a', 'b', 'c', sep=' \ ')

# 여기서 `()`안에 들어가는 모든 것이 인자이다.
```

arg는 _positional argument_, 위치 인자이다. `help(print)`를 통해 확인해보면 `print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`
와 같이 `print`는 'value' 외에도 `sep`, `end`, `file` 등 여러 다른 인자도 받을 수 있다.
위의 `argl` 처럼 `print`가 받는 인자들의 위치를 지켜서 `value`만 넣은 인자를 _positional argument_라고 한다. 
이렇게 넣을 때는 순서를 잘 지켜서 넣어야 할 것이다.

### 4.2. **kwargs
kwarg는 키워드 인자이다. 인자를 'value'만 넣는 것이 아닌 'key=value' 형태로 넣는 것이다.
**위의 `kwargl = print('a', 'b', 'c', flush='True')`는 `flush`이라는 인자를 명시해서 그 값을 `True`로 정해주는 것이 된다.**
 kwarg를 사용할 때의 장점은 함수가 받는 인자의 순서를 무시하고 인자를 명시해줄 수 있다는 것이다. `print` 함수는 여러 인자를 받는데 `flush`인자의 순서는 꽤 뒤에 있다. 이것을 _positional argument_를 사용해서  넣는다면 `flush` 앞의 인자들도 다 정해줘야 `flush`인자에 값을 넣을 수 있을 것이다. 이 때 **kwarg를 사용하면 `flush` 인자를 명시함으로써 인자를 다 적어줘야 하는 불편함을 해소할 수 있는 것이다.**


### 4.3.  _packing과 Unpacking_
4.1과 4.2는 결국 함수의 _unpacking_와 _packing_을 이해하기 위해 사용하는 개념이다. 생각해보자. `print(1,2,3,4,5 ... )`처럼 `print`는 인자의 개수에 제한을 받지 않는다. 왜 그럴까?

#### 4.3.1. _Packing_
_packing_(이하 패킹)은 함수를 정의할 때 사용된다. 우리가 함수를 만든다고 생각해보자. 지금 상황은 `print`처럼 인자의 개수에 구애받지 않는 함수를 절박한 심정으로 만들고 싶은 상황이다. 
이때 패킹은 받는 인자를 하나의 튜플과 하나의 딕셔너리로 묶어서 전달해주는 것을 말한다. 다음 예를 보자.

```python
def myprint(*args, **kwargs):
    string = ''
    for i in args:
        string += str(i)
    for key, value in kwargs.items():
        string += str(value)
    print(string)

myprint(1,2,3,4,k ='?', l = 'ok')

>>> 1234?ok
```
 위의 예는 print를 임의로 다시 정의해본 것이다. 함수를 정의할 때 사용하는 **패킹은 함수가 사용될 때 사용자가 입력하는 모든 positional argument 값들은 args라는 이름의 튜플로, 모든 keyword argument 값들은 kwargs라는 이름의 딕셔너리로 _pack_하겠다는 의지의 천명이다.**

위의 예에서 `args`는 `(1,2,3,4)`의 튜플이고, `kwargs`는 `{'k':'?', 'l':'ok'}`의 값을 갖는 딕셔너리다. 둘은 모두 _iterable_하기 때문에 `for`문을 돌릴 수 있고 그 값들을 `string`이라는 값에 저장하고 그것을 출력한다. 

_아 참고로, args, kwargs는 PEP8에서 제안된 관습적인 표현이다._


#### 4.3.2. _Unpacking_
패킹이 함수를 정의할 때 사용된다면, **_Unpacking_(이하 언패킹)은 반대로 함수를 실행할 때 사용된다.**
```python
from functools import reduce
def myprint(*args):
    for v in args:
        print(v)

list = ['철수', '영희', '불금', '함께 보냈다.']
myprint(*list) ## !!!!!! 중요!

철수
영희
불금
함께 보냈다.
```
myprint라는 함수를 보자. 이 함수에는 먼저 패킹이 사용되었다. **그러니까 함수 실행 시에 받는 인자들을 모두 하나의 튜플로 만들어서 받은 뒤 그 안에서는 `for`문을 돌려 하나씩 출력하고 있다.** 결과는 철수와 영희가 불금을 함께 보냈다라는 내용을 구 하나씩 출력하고 있다.

언패킹은 함수 사용시에 활용된다고 했다. `myprint(*list)`에서 `list` 앞에 `*`가 붙어 있다. 이것이 언패킹이다. 여기서 `*`를 붙이면 _iterable_한 list가 모두 풀어져(unpacking되어) 인자에 들어간다. 그러니까,
> myprint(*['철수', '영희', '불금', '함께 보냈다.'])는 정확히
> myprint('철수', '영희', '불금', '함께 보냈다.') 와 동일하다.


왜 그러면 여기서 언패킹을 했을까? 언패킹을 안 했다고 가정해보자.
> myprint(list)

애스터리스크를 없앴다. 이때는 `lis`t가 문자열을 담은 **리스트 하나로서 함수 안에 들어간다.** 그런데 함수 정의할 때 패킹이 되어 있으므로 `args`는 `list`를 첫 번째 원소로 하는 튜플이 된다.

> args is same with  (['철수', '영희', '불금', '함께 보냈다.'], )

원 함수에서 `args`를 기준으로 `for`문을 돌리게 된다. `args`는 `list`가 아니라 `list`를 포함하고 있는 튜플이다. 즉 `for`문에서 `list`의 문자열 개수만큼 반복되는 것이 아니라 튜플이 가지고 있는 인자 개수 1개만큼만 반복되는 것이다. 

결과물은 ` ['철수', '영희', '불금', '함께 보냈다.']` 리스트 자신이 나왔다. 이것은 우리가 의도한 결과가 아니다. 이럴 때 언패킹을 사용하는 것이다.

정리하자.

타입 | 사용 위치 | 역할 
---- | ------ | ----
**Packing** | 함수 정의할 때 | 함수 실행 시에 받은 모든 원소를 묶고 싶을 때
**Unpacking** | 함수 사용할 때 | 입력하는 리스트, 딕셔너리 등을 풀어서 함수에 넣고 싶을 때

~~이렇게 까지 배우면 빌트인 `sum` 함수의 한계를 뛰어넘을 수 있는 `mysum`을 얼추 구현해볼 수도 있을 것이다. 각자 해보도록 하자.~~



## 5. 지금까지 배운 것을 모두 활용해서 어썸하게 만들자!
2일차의 마지막이다. 우리가 정말 많이 배웠구나... ~~2일차만 5시간 째다..~~ 마지막이다. 오늘 배운 것을 모두 활용해서 어썸하게 코드를 만들자.




### 5.1. FizzBuzz 문제를 확장성 끝판왕 어썸함수로 만들자
이제는 FizzBuzz를 확장성을 더욱더 올려보도록 하자.
1.  람다를 사용해서 짧게 만들어보고
2. *args, **kwargs, 를 사용해서 인자를 무수히 많이 받을 수 있게 하자.

예상되는 함수 형태
> get_awesome_list(100, (3, 'Fizz'), (5, 'Buzz'), (7, 'Ok!'), ('9, Too long'))

```python
def get_awesome_list(n, *args):
    args = list(args)
    args.sort(key=lambda x: x[0])
# ------------------------------------------
"""
위의 두 식은 다음을 위한 것이다. 우리가 받는 arg안의 튜플들의 숫자 순서가 (3,5,7,9)으로 이쁜 순서로 받아들였지만,
세상에는 저 순서를 바꿔서 넣을 불한당들도 존재하기 때문에 위와 같은 식을 썼다.
먼저 튜플에는 sort 기능이 없기 때문에 list로 바꿨고, 
sort식을 사용해서 (3, 5, 7, 9) 오름차순으로 정렬되도록 바꾼 것이다.

이처럼 우리가 만드는 함수나 기능은 분명 어떤 식으로든 개선의 여지나 약점을 없애는 방법이 있다.
그것을 고민하면 분명 더 좋은 함수가 나온다고 혹자는 말한 적이 있다.
"""
# --------------------------------------------

# list comprehension 버전 
    return '\n'.join([''.join([arg[1] if i%arg[0]==0 else '' for arg in args]) for i in range(1, n+1)])
# -------------------------------------------

# --------------------------------------------
# 람다 버전.
    return '\n'.join(map(lambda i: ''.join(map(lambda arg: arg[1] if i%arg[0] == 0 else '' ,args))
    , range(1, n+1)))

print(get_awesome_list(100, (3, 'Fizz'), (5, 'Buzz'), (7, 'Ok!'), (9, 'Too long')))

"""
리스트 컴프리헨션이나 람다나 모양은 다르지만 논리 순서는 똑같다. 이 식들을 풀어쓰면 크게는 `for`문이 두 개가 중첩될 것이다.
일반적으로 람다나 리스트 컴프리헨션에서 상위에 해당되는 `for`문은 다른 `for`문을 감싼다.
위에서도 '1'부터 'n+1'까지의 `for`문이 각각의 숫자를 나누는 `for`문을 감싸고 있다. 핵심은 그거다.
"""

```


<!-- ----------------------------  Reference ---- ----------------- 