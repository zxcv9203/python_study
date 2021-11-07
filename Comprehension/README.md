# Comprehension

Comprehension이란 iterable한 오브젝트를 생성하기 위한 방법중 하나로 파이썬에서 사용할 수 있는 유용한 기능중 하나입니다.

## List Comprehension

List Comprehension은 리스트를 쉽게 생성하기 위한 방법입니다.

파이썬에서 보편적으로 사용되는 기능중 하나로 조금만 응용하면 다양한 조건으로 리스트를 생성할 수 있는 강력한 기능중 하나입니다.

여태까지 학습했던 내용으로 1에서 ~ 10의 길이를 가진 정사각형의 크기를 구하려면 다음과 같이 구현할 수 있을 것입니다.

``` python
areas = []

for i in range(1, 11):
    areas = areas + [i * i]
print(areas)
```

List Comprehension을 이용하면 이를 좀 더 간단하게 구현할 수 있습니다.

``` python
areas2 = [i * i for i in range(1, 11)]
print(areas2)
```

여기서 더 응용해서 짝수의 길이를 가진 정사각형의 크기를 구하려면 다음과 같이 구현해야 할 것입니다.

``` python
for i in range(1, 11):
	if i % 2 == 0:
    	areas = areas + [i * i]
print(areas)
```

이를 List Comprehension을 사용하면 다음과 같이 구현할 수 있습니다.

```python
areas2 = [i * i for i in range(1, 11) if i % 2 == 0]
print(areas2)
```

다음과 같이 for문을 중첩한 상황에서도 List Comprehension을 사용할 수 있습니다.

```
areas3 = [(x, y) for x in range(15) for y in range(15)]
print(areas3)
```

위와 같이하면 x와 y의 값을 하나하나 가져와서 담을 수 있습니다.

## Dict Comprehension