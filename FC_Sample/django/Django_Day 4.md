# Day 4. Models

2016/10/10
박성환

지난 금요일 날 수업한 [모델 부분][day3]에 이어 오늘 나머지 부분을 나가도록 한다.
<br>

#### 1.2.2.4. self reference의 경우 : Symmetrical 
이런 경우를 생각해보자. 사람 모델을 만든다. 사람은 다른 사람과 친구과 될 수 있다. 즉 '관계'가 형성된다. 이렇게 자신 모델과 참조되게 만들어볼 수 있다.

```python
from django.db import models

class Person(models.Model):
    friends = models.ManyToManyField("self")
```
이때는 문제가 없다. 다른 경우를 보자. 트위터를 하는데 내가 다른 사람을 follow할 수 있지만, 그 사람은 안 할 수도 있다. 이렇게 **관계가 비대칭적일 때는 안에 인자로 _symmetrcial=False_**를 넣어준다.

```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    relationships = models.ManyToManyField('self', through='Relationship', 
                                           symmetrical=False, 
                                           related_name='related_to+')

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Relationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

```
`from_person`과 `to_person` 모두 `Person`의 인스턴스이지만 값은 다르다. 상태값을 통해 누가 누구를 향해 펄러우 하는지 알 수 있다.

many to many에서 자신을 참조하는 관계를 정의할 때 중간자 모델을 쓰면, 꼭 `symmetrical=False` 설정을 넣어줘야 한다.


<br><br>
### 1.2.3. One to one
one to one 관계를 정의하기 위해서는 `OneToOneField` 필드를 사용한다.<br>
'유저'와 '상세정보' 라는 테이블이 따로 존재할 때처럼, 객체의 pk를 다른 객체로 확장할 때 유용하다.

ex) 유저 <--> 상제정보. 1대1 매칭.

### 1.2.4. Models across files
완전히 다른 App의 모델을 사용하기 위해서는 
`from geography.models import ZipCode`
처럼 입력해주면 된다. 'geography' 앱의 'ZipCode' 모델을 사용한다는 의미가 된다.


### 1.2.5. Field name restriction
파이썬은 모델 필드 네임을 만들 때 두 가지 제한조건을 둔다.

1. **필드 이름은 파이썬 예약어가 될 수 없다.**
```python
class Example(models.Model):
    pass = models.IntegerField() # 'pass' is a reserved word!
```

2. **필드 네임에는 연속으로 '_'를 두 개 이상 쓸 수 없다.** 장고 모델 api에서 '__'를 사용하기 때문이다.
```python
class Example(models.Model):
    foo__bar = models.IntegerField() # 'foo__bar' has two underscores!

```

SQL 예약어는 문제 없이 사용가능한데, 장고가 SQL 쿼리를 만들 때 다 escape하기 때문이다.

## 1.3. Meta options
모델에 Meta 클래스를 넣어줌으로써 모델에 대한 메타데이터를 넣어줄 수 있다.
```python
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]        # 정렬 시 horn_length 필드를 기준으로 정렬
        verbose_name_plural = "oxen" # 2 마리 이상 표현시 'oxen'으로 표현
```
Meta에 들어갈 수 있는 [옵션][meta]은 정말 많지만 모두 선택적이다.


## 1.4. Model Attributes
**objects** 
---
모델의 가장 중요한 속성은 _Manager_이다. 이것은 데이터베이스 쿼리가 장고 모델에 제공되어 데이터베이스의 리코드를 추출하는 인터페이스이다. 커스텀 매니저가 지정되어 있지 않으면, 기본 이름은 **objects**이다. **매니저는 모델 클래스만을 통해 접근할 수 있고, 모델 인스턴스로는 접근할 수 없다.**

## 1.5. Model Methods
모델에 커스텀 매세드를 추가해 'row-levl' 기능을 각 레코드에 넣을 수 있다. 매니저 메서드가 테이블 단위 작업을 한다면, 모델 메서드는 특정 모델 인스턴스에 작동할 것이다.

Define custom methods on a model to add custom “row-level” functionality to your objects. Whereas Manager methods are intended to do “table-wide” things, model methods should act on a particular model instance.

### 1.5.1. Overriding predefined model methods
데이터베이스를 제어하는 많은 모델 메서드도 커스터마이즈 할 수 있다.  `save()`와 `delete()`의 동작방식을 바꿀 때가 많다.<br>

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
```
위와 같이 깜찍하게 오버라이드 해서 인스턴스의 이름이 Yoko Ono의 경우 세이브를 할 수 없도록 막을 수도 있다.


<br><br><br>
## 1.6. Model inheritance
장고에서의 모델 상속은 파이썬의 상속과 거의 같다. 그러나 상속 방식과 그에 따른 작동 방법이 조금씩 다르다.

### 1.6.1. Abstract base classes.
부모 클래스를 추상클래스로 만든다. 이렇게 되면 부모 클래스는 유명무실해져서 테이블로서 접근하지 않게 된다. 추상클래스는 여러 모델에 적용되는 공통 요소만 추출할 때 사용하면 유용하다.<br><br>

이 추상 부모 모델은 테이블을 만드는 데 사용되지 않는다. 대신, 다른 모델들의 기본 모델이 되어 필드가 자식 클래스에 상속된다. 부모 추상 클래스의 필드와 이름이 같은 필드를 자식 모델이 가지고 있으면 에러가 난다.

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True   		# 추상클래스임을 선언한다!

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

`Student`모델은  `name`, `age`, `home_group`의  세 가지 필드를 가지고 욌다. `CommonInfo`은 추상클래스이기 때문에 일반 장고 모델처럼 사용할 수는 없다. 데이터베이스 테이블도 생성하지 않고, 매니저도 없으며, 인스턴스를 만들거나 자동으로 저장될 수도 없다. <br><br>


### 1.6.2. Multi-table inheritance

장고에서 지원하는 두 번째 상속 방법은 유효한 각 모델이 상속관계를 가지는 것이다. 각 모델은 자신의 데이터베이스 테이블과 응답하여 쿼리 받고 생성될 수 있다. 상속 관계는 자식 모델과 각 부모 모델이 자동생성되는 `OneToOneField`를 통해 연결된다.

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```

모든 데이터가 서로 다른 데이터베이스 테이블에 있음에도, `Place`의 모든 필드는 `Restaurant`에서도 사용가능하다.
```python
>>> Place.objects.filter(name="Bob's Cafe")
>>> Restaurant.objects.filter(name="Bob's Cafe")
```

multi-table inheritance상속에서는 자식 클래스가 부모의 메타 클래스를 상속받는다는 것은 말이 되지 않는다. 복잡한 상속관계 속에서 메타 옵션들이 모두 상속, 적용되면 에러로 연결되기 쉬울 것이다.(**abstract base class와는 다르다!**)<br><BR>

그래서 자식 모델은 부모의 메타클래스에 대한 접근권한이 없다. 그러나, 예외가 몇 가지 있는데 자식이 `ordering`이나 `get_latest_by` 속성은 자식이 명시하지 않으면 상속받는다.



### 1.6.3. Proxy inheritance
'proxy'는 영어로 '대리인'이라는 뜻이다. proxy 상속이 딱 그렇다.
다중 테이블 상속의 경우 서브 클래스나 모델을 위한 테이블이 새로 생성되었다. 이것이 일반적인 경우이지만 그렇지 않은 경우도 있다. 모델의 행동방식을 잠시 바꾸는 것을 원할 때 proxy 상속을 사용하면 된다.<br><br>

proxy 상소고을 사용하면 오리지널 모델에 대한 대리인이 생성된다. proxy 모델에서 만들고, 지우고, 업데이트하면 오리지널 모델을 사용한 것처럼 사용될 것이다. 차이점이 있다면 오리지널의 일반적인 작동방식과는 다르게 오리지널 모델을 컨트롤한다는 점이다.

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass
```
**`MyPerson`이라는 모델에서만 `do_something` 메서드를 사용할 수 있다. 하지만 적용효과는 `Person` 모델이 받는다.**

<br><br><br><br>


# 2. Model field reference¶
모델 필드를 정리한다. 시간상 너무 특수해보이는 것은 제외했다.


##  2.1. Field options

### 2.1.1. null and blank
1. `blank` : True이면 해당 필드는 빈값이 들어와도 된다. validation-related.
2. `null` : 데이터베이스에서 빈 값이 오면 null이 저장된다. datatbase-related.


### 2.1.2. db_column
해당 필드에 사용할 데이터베이스 이름이다. 없으면, 필드 변수 명을 이름으로 사용한다.
이름에 SQL 예약어를 사용해도 장고 내부에서 escape해주기 때문에 상관없다.

### 2.1.3 db_index¶
True이면, 이 필드를 위해 데이터베이스 인덱스가 생성된다.


### 2.1.4 default
필드의 기본값을 설정한다. 값일 수도 있고, 함수일 수도 있다. 함수라면, 인스턴스가 생성될 때마다 실행될 것이다.<br><br>

default 값은 list, set처럼 mutable한 값을 사용할 수 없다. 왜냐하면 함수는 모듈 로드시 단 한 번의 인자 세팅을 하기 때문이다. 모든 인스턴스가 한 리스트를 공유하기 바라지는 않을 것이다.<br><br> 

대안은 함수로 객체를 반환하는 것이다.
```python
def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)
```
이러면 인스턴스가 생성될 때마다 새로운 딕셔너리가 반환될 것이다.



### 2.1.5. editable
기본은 True이며 해제되어 있을 경우 값을 바꿀 수 없다. admin 사이트에서나 다른 form에서 보이지 않는다. model validation에서도 보이지 않는다.


### 2.1.6. unique_for_date

 DateField나 DateTimeField에 사용해서 날짜값이 중복되지 않게 한다.
` unique_for_date="pub_date"` 만약 이런 옵션을 갖는 필드가 있다면, 장고는 pub_date가 가지고 있는 날짜 값은 인스턴스로 생성될 수 없도록 할 것이다.

unique_for_year, unique_for_month는 연과 월이 겹치지 않게 한다.


<br><Br>
## 2.2. Field Types

### 2.2.1 AutoField
적절한 ID 값에 맞게 자동으로 증가하는 정수 필드이다. 이것을 직접적으로 쓸 일은 많이 없는데, 보통 장고에서 이 필드를 사용한 id 값을 자동생성하기 때문이다. 

### 2.2.2. BooleanField
true/false 필드이다. 이 필드에 대응되는 기본 form은 CheckboxInput이다.
null 값을 받을 필요가 있다면 NullBooleanField를 대신 사용한다.<br>
BooleanField의 기본값을 지정해주지 않으면 None으로 초기화된다.


### 2.2.3. CharField(max_length=None)
크고 작은 문자열에 대응하는 문자열 필드이다. 긴 글의 경우 `TextField`를 사용해라. 기본 form은 TextInput이다. 그리고 최대길이를 지정하는 `max_length`인자를 꼭 가져야 한다.

### 2.2.4. DateField(auto_now=False, auto_now_add=False, **options)
파이썬 datetime.date 인스턴스가 저장된다. 몇몇 인자를 가지고 있다.

#### 2.2.4.1. auto_now
인스턴스가 저장될 때마다 자동으로 시간을 새로 지정한다. '최근 수정된' timestampf를 다룰 때 유용하다. 시간은 언제나 현재 시간이 사용되며, override할 성격의 것이 아니다.<br><BR>

이 필드는 `save` 메서드를 사용할 때마다 자동으로 업데이트 되는데, `QuerySet.update()`와 같이 다른 필드를 업데이트하는 방식으로는 변경되지 않는다.

#### 2.2.4.2. auto_now_add

객체가 **생성되었을 때** 값을 업데이트 한다. 생성 timestamp를 만들 때 유용하다. 언제나 현재값이 사용되며 오버라이드할 수 없다. 그래서 객체를 만들 때 값을 지정해도 무시될 것이다.

**`auto_now_add`, `auto_now`, `default`는 상호배제적이기  때문에 두 개 이상 가이 사용할 수 없다.**



#### 2.2.4.3. DateTimeField(auto_now=False, auto_now_add=False)

위의 DateField와 비슷하지만 datetime.datetime의 객체로 시간까지 저장할 수 있다.

#### 2.2.4.4. DurationField(**options)

시간의 경과를 저장하는 필드이다. 파이썬의 `timedelta`를 모델로 했다. 포스트그래 SQL를 제외한 모든 데이터베이스에서 DurationField와 DateTimeField는 연산이 되지 않는다.

#### 2.2.4.5. EmailField(max_length=254)
값이 적절한 이메일 주소인지 확인하는 CharField이다. 값을 검증하기 위해 EmailValidator를 사용한다.

#### 2.2.4.6. FileField(upload_to=None, max_length=100, )
파일을 업로드하는 필드이다. primary_key와 unique 속성을  받을 수 없다.


#### 2.2.4.7. FloatField
소수를 표현하는 필드로 파이썬의 `float` 인스턴스를 표현한다.
DecimalField와 다르다.

#### 2.2.4.8. ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

FiledField의 모든 속성과 메서드를 상속받고, 추가로 적절한 이미지인지도 확인한다.
FileField에만 적용되는 특수한 속성과 더불어 `height_field`, `width_field` 속성도 가지고 있다.
1. height_field : 인스턴스가 저장될 때마다 자동생성될 모델 필드이다. 이미지의 높이를 저장한다.
1. width_field : 인스턴스가 저장될 때마다 자동생성될 모델 필드이다. 이미지의 너비를 저장한다.

#### 2.2.4.9. IntegerField
정수를 담는 필드이다.  -2147483648부터  2147483647까지의 값을 담는다. 양수만을 담는 PositiveIntegerField가 있고, 값이 커진 BigIntegerField가 있다.


#### 2.2.4.10  GenericIPAddressField(protocol='both', unpack_ipv4=False)


IPv4나 IPv6 주소를 문자열 형식으로 담는 필드이다.(e.g. 192.0.2.30 or 2a02:42fe::4). <br><BR>

특수한 인자가 있다.
1. protocol
 'IPv4' 만 받거나  'IPv6'만 받을 수 있고, 또는 'both' (default), 모두를 받을 수도 있다. 기본값은 'both'이다.

2. unpack_ipv4
True이면 `' ::ffff' --> '192.0.2.1'` 와 같이 숫자형식으로 unpack한다. 


#### 2.2.4.11  URLField(max_length=200)
URL을 위한 CharField이다. CharField의 다른 모든 서브 클래스들과 같이, `max_length` 인자를 받는다. 기본은 200이다.




[day3]:https://github.com/shoark7/FastCampus_WPS/blob/master/FC_Sample/django/Django_Day%203.md
[meta]:https://docs.djangoproject.com/en/1.10/ref/models/options/
