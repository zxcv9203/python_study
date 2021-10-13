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