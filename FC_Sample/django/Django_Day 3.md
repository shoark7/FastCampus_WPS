# Day 3. Models


##  1. [Introduction to models](https://docs.djangoproject.com/en/1.10/topics/db/models/)

모델은 정보에 대한 단일하고 확정적인 원천이다. 모델은 정보에 대한 필수적인 필드와 행동을 담고 있다. 일반적으로, 각각의 모델은 하나의 데이터베이스 테이블과 매핑된다.

기본은,
* 각각의 모델은 파이썬 `django.db.models.Model`을 상속받는 클래스이다.
* 모델의 속성은 데이터베이스의 필드를 나타낸다.
* 이것들을 통해, 장고는 데이터베이스에 접근할 수 있는 자동생성 API를 제공한다.

<br>
 모델을 만든 후 장고에게 모델을 만들었으니 사용한다고 선언해야 한다. 그때 `settings.py`의 `INSTALLED_APPS` 리스트에 우리가 만든 앱을 넣어줘야 한다.<Br>
 이때, 문자열로 앱을 추가하기 때문에, 따로 import해줄 필요가 없으며 'makemigrations', 'migrate'해줘야 최종적으로 사용 가능하다.
 
 
### 1.1. Fields
#### 1.1.1.
데이터베이스 테이블에서 Field(이하 필드)는 꼭 필요하다. 필드는 클래스 속성으로 표현되며, 'clean', 'save', 'delete' 등은  model API로서 이름으로 사용해서는 안 된다.

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

```
`Musician`, `Album`은 테이블이고 , `first_name`, `instrument` 등은 필드라고 한다.

<br>
### 1.1.2. Field type
테이블의 필드는 'Field'를 상속 받는 클래스의 객체여야 한다. 아무 속성이나 다 필드가 되는 것은 아니다.
각 필드는 특정 HTML widget과 연결되어 있어 admin 사이트나 html 페이지에서 형식에 맞는 값을 선택하고 입력할 수 있다.

<br>
### 1.1.3. Field options
각각의 필드는 자신의 고유한 인자를 받아야 한다. CharField가 max_length를 가져야 하는 것이 그 예라고 할 수 있다.<br> 또한 모든 필드에 사용할 수 있는 인자들도 있다. 그런 인자들은 필수가 아닌 선택이다. 인자들은 정말 많지만 그 중 필수적인 것들만 알아보자.<br>

**null**<br>
이 옵션이 True로 켜져 있으면 데이터베이스에서 빈 값을 null로 저장할 것이다. 기본은 False이다.<br><br>
**blank**<br>
이 옵션은 값이 비어도 된다. 기본은 False이다. **`null`과 `blank`의 차이는 `null`이 데이터베이스 측면에서 빈 값을 처리하는 방식이라면 `blank`는 장고(파이썬) 측면에서 빈 값을 관리하는 방식이다.**<br><br>
**choices**<br>
두 개의 튜플로 이루어진 리스트, 튜플로서 이 값이 주어저 있으면 매우 긴 문장을 데이터베이스에는 짧게 줄인 문장으로 넣는 것이 가능해진다.<br>

```python
from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```

사람이라는 테이블은 입는 셔츠사이즈를 필드로 받는다고 하자. <br>
'small', 'medium', 'large' 라는 긴 값을 다 넣을 필요 없이 데이터베이스에는 'S', 'M', 'L'만 넣어도 이해하기에는 충분할 것이다.<br>
**이때 `SHIRT_SIZES`라는 튜플로 이루어진 튜플을 만들고, `shirt_size`필드에 `choices` 인자를 넣어준다. 이제 사람 레코드를 만들 때, 셔츠 사이즈를 'S', 'M', 'L'과 같이 짧게 넣게 된다.**<br>

```python
p = Person(name="Fred Flintstone", shirt_size="L")
p.save()
p.shirt_size
>>> 'L'

p.get_shirt_size_display()
>>> 'Large'
```

다음과 같이 장고 쉘을 실행시켜 `Person`테이블에 `p`라는 레코드를 입력했다. `p.shirt_size`, 그러니까 데이터베이스에 들어가는 값은 짧게 나온다. 그런데 파이썬을 통해 긴 값을 보고 싶다면
`record.get_foo_display()`<br>
함수를 사용하면 긴 값을 구할 수 있다.<br>

**default**<br>
필드의 기본값을 지정해줄  수 있다. 상수, 변수뿐 아니라 callable한 함수도 들어갈 수 있다. <br><br>

**help_text**<br>
form 위젯에 추가적인 도움말이 표시된다. 이건 특히 필드가 form에서 사용되지 않을 때에도 문서화에 도움이 된다.<br><br>

**primary_key**<br>
True이면, 이 필드는 테이블의 primary key가 된다. **만약 모델에서 primar key가 하나도 선언되어 있지 않으면 장고는 자동으로 정수 단위로 증가하는 primary key를 추가**하며 따라서 primary key를 넣어주지 않아도 상관 없다. 그 필드의 기본이름은 'id'가 된다.<br>
primary key는 읽기 전용이다. 만약 어떤 레코드의 primary key를 변경하고 그 값을 저장하려고 한다면, **다른 값들과 달리 값이 저장이 안 되고 새로운 레코드가 생성된다.**<br><br>

**unique**
적용되어 있으면 이 필드의 데이터들은 유니크해야 한다.<br> primary key와의 차이는 primary key는 다른 테이블과의 연결에서 핵심적인 역할을 하겠다는 중요도가 포함되어 있다면, unique는 단순히 겹치지 않게 하겠다는 의미가 있다. 그래서 primary key가 더 중요하다.<br><br>


### 1.1.4. 자동으로 증가하는 필드
테이블에서 primary key를 주지 않으면 장고는 기본적으로 이 필드를 테이블에 추가한다.
`id = models.AutoField(primary_key=True)`
이것이 자동 증가하는(auto_incremental) primary key이다. 이름을 변경하는 것과 같이 이 값은 얼마든지 변경할 수 있으며 primary key를 따로 지정해주면 적용되지 않는다.<br><br>


### 1.1.5. verbose filename
ForeignKey, ManyToManyField and OneToOneField를 제외한 각각의 필드타입은 첫 위치인자로 verbose name을 받는다.<br>만약 주어지지 않으면, 장고는 자동으로 필드 속성이름에서 '_'를 ' '로 바꾸어 verbse name을 만들 것이다.<br>

foreignKey, ManyToManyField,  OneToOneField키는 첫 번째 인자로 model class를 받아야 하기 때문에 verbose name을 keyword 인자로  받아야 한다.

<br><br><br><br>


## 1.2. Relationships
#### ~~주의 : 데이터베이스에 대한 최소한의 이해가 없으면 알아듣기 힘듭니다.~~
장고문서에서는 관계형 DB의 진정한 힘은 테이블을 서로 연결시키는 데 있다고 강조하고 있다. 장고는 테이블간  many-to-one, many-to-many and one-to-one, 이렇게 세 가지 경우에 대응가능하도록 만들어 놓았다. **관련된 모드 필드들은 첫 번째 위치인자로 Model instance를 받아야 한다.**

### 1.2.1. many to one relationship
이 관계는 장고에서 차와 생산자의 관계를 들고 있다. 차는 자신을 만든 한 명의 생산자를 가질 수 있다. 그런데 생산자는 여러 차를 생산할 수 있다.<br> **차, 생산자 테이블과 같은 many to one관계는 ForeignKey로 관계를 정의한다.**<br>

```python
from django.db import models

class Manufacturer(models.Model):
	pass

class Car(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	pass
```

이렇게 테이블을 구성할 수 있을 것이다. 이때 핵심적인 문장은 다음과 같다.
`manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)`
1. `Car`테이블은 생산자를 첫 인자로 받는 ForeignKey를 가진다.<br>
필드의 이름은 관습적으로 관계 맺는 테이블의 lowercase로 하는 경우가 많다.
2. 관계는 'many to one'이다. 여기서 'one'의 `Car`에 ForeignKey를 넣는다.<br> `on_delete=models.CASCADE`는 관계 맺고 있는 테이블 예를 들어, 생산자 현대자동차가 망한다면 그와 관계 맺고 있던 `Car` 레코드들까지 같이 지워진다는 의미를 갖고 있다.

```python
class Manufacturer(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return 'Manufacturer : {}'.format(self.title)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    def __str__(self):
        return "Car : {}".format(self.title)
```
생산자와 자동차의 테이블을 만들었다. 두 테이블은 many to one의 관게에 있어 자동차에 ForeignKey 필드를 넣었다. 
`def __str_` 넣어줌으로써 구분이 어려운 object로 출력되지 않도록 했다.


```python
m1 = Manufacturer.objects.create(title='현대자동차')
m2 = Manufacturer.objects.create(title='도요타')
m3 = Manufacturer.objects.create(title='기아자동차')

c1 = Car.objects.create(manufacturer=m1, title='소나타')
c2 = Car.objects.create(manufacturer=m2, title='엔진엑스')
c3 = Car.objects.create(manufacturer=m2, title='기아엑스')
```
생산자와 자동차의 레코드를 세 개씩 만들었다. 자동차 인스턴스를 만들 때 생산자가 인자로 들어간다는 것이 중요하다.
자동차에서는 `c1.manufacturer`를 통해 생산자 정보에 대해 접근이 가능하다. 반대로 생산자는 어떨까? m1, m2, m3는 필드로 자동차와 관련한 항목이 없다.
오직 이름(title)만 있을 뿐이다. 장고는 생산자에서 자동차에 접근할 수 있는 방법을 제공해준다. 
`many.foo_set` 셋처럼 소문자로 '_set'을 붙여주면 역으로 생산자가 자동차에 접근할 수 있다.

```python
m1.car_set.all()
>>> <QuerySet [<Car: Car : sonata>, <Car: Car : avante>]>
```
다음과 같이 생산자가 갖는 다수의 자동차를 확인할 수 있다. 또 생산자가 또 다른 차를 만들었다면

```python
m1.car_set.add(c2)

c2.manufacturer

>>>   현대자동차
```

와 같이 값을 확장할 수 있다. 이때 차는 언제나 하나의 생산자만을 가져야 한다. 
그래서 `m1.car_set.add(c2)`를 통해 생산자는 문제없이 생산하는 차를 늘일 수 있는데,<br> 
`c2`의 경우 생산자는 하나만 가져야 하기 때문에 기존의 생산자가 `m2`이였지만 윗 문장을 통해 `m1`으로 바꼈다는 것을 확인할 수 있었다.
<br><br>

### 1.2.2. Many to many

#### 1.2.2.1 기본적인 경우
many-to-many 관계를 정의하기 위해서는 `ManyToManyField`를 사용한다. 다른 필드 타입처럼 사용할 수 있는데 첫 위치인자로 관계 맺은 모델을 받아야 한다.<br>
예를 들어보자. 피자와 피자에 들어가는 토핑! 피자는 여러 토핑이 올라가고(many), 하나의 토핑은 여러 피자에 들어간다.(many) 구현해보자.

```python
from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=20,)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=20, )
    toppings = models.ManyToManyField(Topping)
    def __str__(self):
        return self.name
```

핵심은 `toppings = models.ManyToManyField(Topping)` 이 문장이다. 
다 대 다 관계라고 해서 'ManyToManyField'를 두 테이블에 모두 쓸 필요는 없다.(정확히는 안 된다.)<br> 
하나의 테이블에 넣는데 일반적인 관념에서 피자가 토핑을 갖지, 토핑이 피자를 여러 개 갖지 않는다.<br>
그래서 관습적으로 Pizza 역할에 필드를 넣고, 변수 이름을 _lowercase+'s'_로 짓는다.<br><br>

```python
t1 = Topping.objects.create(name='망고')
t2 = Topping.objects.create(name='사과')
t3 = Topping.objects.create(name='고구마')

p1 = Pizza.objects.create(name='p1피자')
p2 = Pizza.objects.create(name='p2피자')
p3 = Pizza.objects.create(name='p3피자')
```

이렇게 레코드를 세 개씩 만들었다. 여기서 위화감을 느낀 사람이 있는가?<br>
위의 ForeignKey와 큰 차이가 있는데 **피자의 레코드에서 toppings 필드 값을 입력하지 않았다.**<br>
애초에 들어가면 에러가 난다. 위의 경우 하나의 차는 한 대의 생산자만 가질 수 있었다. 그래서 생성할 때 기본 인자값으로 하나만 받으면 문제가 없었다.<br>
하지만 피자, 토핑의 경우에는 둘 다 상대방을 많이 가질 수 있으며 그래서 피자가 토핑을 가지고 생성되는 것이 의미가 없고(어차피 추가하는 과정이 필요하고),
데이터베이스 측면에서 쉽게 저장할 수도 없다. 그러면 어떻게 토핑을 추가해야 할까?

```python
p1.toppings.add(t1, t2)
p2.toppings.add(t2, t3)

t1.pizza_set.add(p1)
t2.pizza_set.add(p3)
```
이렇게 추가한다. 이때 피자의 경우 Topping이 아닌 아까 이름 지어준 `toppings`라는 데 유의한다.<br>
이렇게 만들어주면 내부적으로는 둘의 사이를 잇는 중간 테이블이 생성되는데 그 테이블의 이름은 'Pizza_toppings'이 된다. 
그리고 이 테이블은 각각의 관계를 모두 저장한다. 다음과 같을 것이다.

ID | Pizza ID | Topping ID
--- | --- | ---
1  | 1 | 2
2 | 1 | 3
3 | 2 |1
4 | 2 | 3
5 | 3 | 2
6 | 3 | 3

이 테이블과 연결되면 가령 '피자 아이디 3이 갖는 모든 토핑을 구하라'와 같은 쿼리가 들어오면 이 테이블에서 필터링을 하면 구할 수 있을 것이다.<br>

#### 1.2.2.2. intermediate model을 사용한 경우
간단한 many to many 관계를 다룬다면 위의 경우만으로 충분할 것이다. 
그러나, 가끔 두 테이블를 단순히 잇는 것이 아니라 테이블들의 관계에 관한 _데이터_ 자체를 다뤄야 하는 경우가 생길 수 있다.<br><br>

예를 들어, 소속사와 소속 음악가를 다뤄야 하는 애플리케이션을 생각해보자. 이
들 사이에는 다 대 다 관계가 적용될 것이다. 이 관계에는 음악가가 소속사를 들어간 날짜와 같이 또 수집하고 싶은 정보가 있을 수 있다.<br><br>

이것을 `membership`이라는 중간 테이블로 만들어서 원하는 자료를 저장할 수 있을 것이다. 이때 장고는
_intermediate model_을 지원한다. 코드를 보자.

```python
class Person(models.Model):

    name=models.CharField(max_length=10)
    def __str__(self):
        return "Person : "+self.name

class Group(models.Model):

    name = models.CharField(max_length=20)
    members = models.ManyToManyField(Person, through='Membership')
    def __str__(self):
        return "Group : "+self.name

class Membership(models.Model):

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=50)

```
`members = models.ManyToManyField(Person, through='Membership')`가 중요하다.
일반적인 다 대 다 관계와 비슷해 보이는데,`through='Membership'` 라는 인자가 들어 있다.<br>
그리고 Membership이라는 모델느 `person`과 `group`이라는 ForeignKey를 갖는다.<br>
아까 차와 생산자에서 'one' 관계인 차에 'ForeignKey'가 들어간 것 기억하는가? Membership에 키가 들어간 것이 그래서이다. 
멤버십 인스턴스는 하나의 그룹 또는 소속원을 갖는데 한 소속원은 Membership을 통해 많이 들어갈 수 있다.<br>

피자, 토핑과 달리 여기는 단순히 관계뿐만 아니라 날짜, 초청 이유까지 들어가야 해서 **`p1.group_set.add`, `g1.members.add()`를 쓸 수 없다.**




