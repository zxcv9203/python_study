# 클래스와 객체지향 프로그래밍

## 자료형 확인하기

어떤 변수가 무슨 자료형인지 확인하고 싶을 때 type을 사용해서 확인할 수 있습니다.

type을 이용해서 자료형을 확인하는 방법은 다음과 같습니다.

```python
type(value)
```

다음은 type의 사용 예시입니다.

```python
s = "hello world"
print(type(s)) # <class 'str'>
f = 3.14
print(type(f)) # <class 'float'>
```

아래와 같이 같은 수임에도 자료형이 다른 경우가 있습니다.

```python
i = 42
print(type(i)) # <class 'int'>
f = 42.0
print(type(f)) # <class 'float'>
```

이 경우 `==`로 연산할 경우 True가 나옵니다.

``` python
print(i == f) # True
```

해당 값이 해당 자료형인지 확인하고 싶을때는 `isinstance`를 사용하여 확인할 수 있습니다.

``` python
isinstance(value, type)
```

다음은 사용예시입니다.

```python
i = 42
print(isinstance(i, int)) # True
print(isinstance(i, float)) #false
```

## 클래스와 인스턴스

앞서 자료형을 type을 이용해서 확인할때 출력 값으로 class 라는게 앞에 붙어 나온것을 보셨을 것입니다.

```
<class 'str'>
```

클래스란 무엇일까요?

클래스란 `함수나 변수들을 모아 놓은 하나의 집합체`를 의미합니다.

그리고 이 `클래스를 이용해서 생성된 객체`를 인스턴스라고 합니다.

인스턴스는 각자 자신의 값을 가지고 있습니다.

예를들어, 사람이 있으면 사람마다 각각의 이름이 있을 것입니다.

이름이 다르다고 사람이 아닌 것은 아니지만 이 두개를 같다고 볼 수 는 없을 것입니다.

그리고 이름이 같다고해도 서로 다른 두 사람이 완전히 똑같은 사람이라고 할 수는 없습니다.

여기서 사람을 클래스로 비유할 수 있고, 각 각의 이름을 가진 사람을 인스턴스라고 부를 수 있습니다.

## 클래스 만들어보기

클래스를 생성할때는 다음과 같이 생성할 수 있습니다.

```py
class className():
```

예를들어 다음과 같은 형태로 선언할 수 있습니다.

```py
class Human():
	#code..
```

만든 클래스로 인스턴스를 생성하고 싶을 경우 함수를 호출하는 것처럼 클래스이름에 괄호를 붙여 사용할 수 있습니다.

```py
var = class()
```

다음은 사용예시입니다.

```py
person = Human()
```

생성한 인스턴스는 같은 변수이름이라도 다른 값을 가질 수 있습니다.

```py
person1.lang = "한국어"
person2.lang = "English"
```

다음과 같이 함수를 넣어서 사용할 수도 있습니다.

```py
def speak(person):
    print("{}이 {}로 말을합니다".format(person.name, person.lang))
Human.speak = speak
person1.speak()
person2.speak()
```

클래스와 인스턴스를 사용하지 않더라도 문제를 해결할 수 있겠지만 데이터와 코드를 사람이 이해하기 쉽게 포장할 수 있는 장점이 있습니다.

## 모델링

이번엔 한번 직접 사람을 나타내는 Human이라는 클래스를 만들어봅시다.

Human클래스에 실제 사람처럼 이름과 몸무게 같은 정보를 다음과 같이 집어넣어봅시다.

```py
class Human():
    '''인간'''
def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human
person = Human.create("yongckim", 99)
```

이번엔 실제사람이 걷다보면 몸무게가 줄어드는 것처럼 walk 라는 함수를 호출하면 몸무게가 줄도록 구현해봅시다.

```py
def walk(person):
    person.weight -= 0.1
    print(" {}가 걸어서 {}kg가 되었습니다.".format(person.name, person.weight))
```

위와 같은 맥락으로 음식을 먹으면 몸무게가 증가하기 위해서 eat이라는 함수를 만들어봅시다.

```py
def eat(person):
    person.weight += 0.1
    print(" {}가 먹어서 {}kg가 되었습니다.".format(person.name, person.weight))
```

다음과 같이 만든 함수들을 실행해봅시다.
```py
Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()
```

위의 코드를 실행해보면 몸무게가 줄었다 늘고 다시 줄어드는 것을 볼 수 있습니다.

위의 구현한 것과 같이 현실 세계의 개념을 가져와서 클래스로 표현하는 것을 모델링이라고 합니다.

## 메소드

메소드란 클래스에 묵여서 클래스의 인스턴스와 관계되는 일을 함수입니다.

메소드로 사용하기 위해서는 다음과 같이 클래스에 함수를 넣기만하면됩니다.

```py
class Human():
    '''인간'''
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person
    def eat(person):
        person.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))
    def walk(person):
        person.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))
```

> self

메소드를 호출할 때 첫번째 인자는 자동으로 자기자신이 들어가게 됩니다.

이때 첫번째 인자를 관례적으로 self라고 부릅니다.(다른 이름으로 사용가능)

```py
class Hello:
	#code 생략
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))
person.walk()
```

위의 코드의 경우 person이 self의 매개변수로 들어가게 됩니다.

만약 매개변수가 여러개일 경우 self 이후만 다음과 같이 괄호안에 적으면 됩니다.

```py
class Hello:
	#code 생략
    def speak(self, message):
        print(message)
person.speak("안녕하세요.")
```

## 특수한 메소드

> `__init__`

파이썬에는 오브젝트를 생성할 때 자동으로 초기화할 수 있게해주는 `__init__`함수가 존재합니다.

```py
class Human():
    '''인간'''
    def __init__(self, name, weight):
        '''초기화 함수'''
        self.name = name
        self.weight = weight
        print("__init__실행")
person = Human("yongckim", 666)
```

위 코드를 실행하게 되면 `__init__`을 호출하지 않았음에도 함수가 실행되는 것을 볼 수 있습니다.

> `__str__`

만약 인스턴스를 자체 출력을 하면 다음과 같이 오브젝트의 주소위치가 나옵니다.

```
<__main__.Human object at 0x7f9ad688cfd0>
```

만약 인스턴스 자체 출력을 할때 다른 형식을 지정해주고 싶으면 `__str__`로 출력형식을 지정할 수 있습니다.

```py
class Human():
    '''인간'''
    def __str__(self):
        '''문자열화 함수'''
        return "{} ( 몸무게 {}kg )".format(self.name, self.weight)
person = Human()
print(person)
```

위의 코드를 실행시키면 주소가 아닌 `__str__`에서 반환하는 문자열이 출력됩니다.