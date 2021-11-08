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

Dictionary도 Comprehension으로 생성할 수 있습니다.

{}안에 식의 부분에 키와 값 2개를 `key : value`와 같이 지정하여 작성하면 됩니다.

다음과 같은 리스트를 만들어봅시다.

```python
students = ["yongckim", "yongcpark", "yongclee"]
for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number, name))
```

위의 파이썬 코드는 0번부터 시작한다는 문제점이 있습니다.

이를 dict Comprehension을 이용해서 해결하면 다음과 같이 작성할 수 있습니다.

```python
std_dict = {"{}번".format(number+1): name for number, name in enumerate(students)}
print(std_dict)
```

### zip
zip 함수는 여러개의 iterable한 객체를 인자로 받고 각 객체가 담고 있는 원소를 튜플 형태로 받을 수 있습니다.

```python
students = ["yongckim", "yongcpark", "yongclee"]
scores = [85,92,78]
for x, y in zip(students, scores):
    print(x, y)
```

다음을 실행하면 students와 scores의 같은 인덱스의 값이 묶여 출력됩니다.

다음과 같이 zip과 dict comprehension을 이용해서 dictionary 형태로 값을 저장할 수 있습니다.

```python
score_dic = {student : score for student, score in zip(students, scores)}
print(score_dic)
```