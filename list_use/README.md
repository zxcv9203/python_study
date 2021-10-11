# List의 다양한 기능

## List에서 특정 값의 인덱스 위치를 알고 싶을 때

index를 이용해서 특정 값의 인덱스 위치를 알아낼 수 있습니다.

다음과 같은 형태로 사용합니다.

```python
list.index(value)
```

다음은 사용 예시입니다.

```python
list1 = [1, 2, 3, 4, 5]
print(list1.index(4))
```

존재하지 않는 숫자를 값에 넣을 시 다음과 같은 ValueError가 발생합니다.

```python
list1 = [1, 2, 3, 4, 5]
print(list1.index(11))
```
```
ValueError: 11 is not in list
```

또한 같은 값이 여러개 존재할 경우 가장 첫번째로 나오는 값의 인덱스가 출력됩니다.

```python
list1 = [1, 1, 1, 1, 1]
print(list1.index(1)) # 0 출력
```

## List 뒤에 값을 추가하는 방법

리스트 간 더하기 연산을 하면 리스트를 합칠 수 있습니다.

다음과 같은 형태로 사용합니다.

```python
list = [1, 2, 3] + [4, 5, 6]
list += [7, 8, 9]
```

다음은 사용 예시입니다.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2
print(list3) # [1, 2, 3, 4, 5, 6]

list1 += list2
print(list1) # [1, 2, 3, 4, 5, 6]
```

extend를 이용해서도 리스트에 값을 추가할 수 있습니다.

다음과 같은 형태로 사용합니다.

```python
list.extend([1, 2])
```

다음은 사용예시 입니다.
```python
list4 = [1, 2, 3]
list4.extend([5, 6, 7])
print(list4) # [1, 2, 3, 5, 6, 7]
```

주의해야할 점은 리스트끼리만 합치는 것이 가능합니다.

예를들어 다음과 같은 연산은 불가능합니다.

```python
list5 = [1, 2, 3]
list6 = list5 + 3 # TypeError

list5.extend(3) # TypeError
```

참고로, extend가 +를 이용해서 합치는 것보다 성능이 더 좋습니다.

## List에서 특정 위치에 값을 추가하고 싶을 때

insert 키워드를 이용해서 추가할 수 있습니다.

다음과 같은 형태로 사용합니다.

```python
list.insert(index, value)
```

첫번째는 인덱스 두번째는 넣고 싶은 값을 집어 넣으면 됩니다.

다음은 사용 예시입니다.

```python
list1 = [1, 2, 3]
list1.insert(2, 99) # [1, 2, 99, 3]
```

위와 같이 사용하면 list1에 두번째 인덱스에 99라는 값이 들어갑니다.

inset에 인덱스 부분에 음수로도 접근이 가능합니다.

음수로 접근할경우 리스트의 마지막 부터 접근합니다.

예를들어 다음과 같이 사용한다고 합시다.

```python
list1 = [1, 2, 3]
list1.insert(-1, 10) # [1, 2, 10, 3]
```

가장 마지막 인덱스가 2이기 때문에 2번째에 10이 들어갑니다.

만약 인덱스가 리스트의 최대 인덱스 보다 클 경우 맨 마지막에 하나가 추가됩니다.

```python
list1 = [1, 2, 3]
list1.insert(6, 10)
print(list1) # [1, 2, 3, 10]
```

## List 오름차순 정렬하기

리스트를 오름차순으로 정렬하고 싶으면 sort를 사용해서 정렬 할 수 있습니다.

다음과 같이 사용할 수 있습니다.

```python
list.sort()
```

## List 내림차순 정렬하기

리스트를 내림차순으로 정렬하고 싶으면 reverse를 사용해서 정렬할 수 있습니다.

다음과 같이 사용할 수 있습니다.

``` python
list.reverse()
```