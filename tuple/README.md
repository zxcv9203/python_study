## 튜플 만들기
+ 한번 정해진 순서를 바꿀 수 없다.
+ 튜플 선언
```python
tuple1 = (1,2,3,4)
tuple2 =  1,2,3,4
mylist = [1,2,3,4]
tuple3 = tuple(mylist)
```
+ 튜플은 값의 변경과 삭제가 불가능

## packing
+ 하나의 변수에 여러개의 값을 넣는 것

## unpacking
+ 패킹된 변수에서 여러개의 값을 꺼내오는 것
```python 
c = (3, 4) 
d, e = c  # c의 값을 언패킹하여 d, e에 값을 넣었다.
f = d, e  # 변수 d와 e를 f에 패킹했다.
```

## 튜플의 활용
+ 두 변수의 값을 바꿀 때 임시 변수가 필요 없다.
```python
x = 10
y = 5
x,y = y,x # x = 5, y = 10
```
+ 함수의 리턴 값으로 여러 값을 전달 할 수 있다.
  
## 튜플 리스트 활용
```python
# enumerate는 인덱스([0])와 값([1])을 동시에 가져오는 함수이다
for a in enumerate(list):
    print('{}번째 값: {}'.format(a[0], a[1])
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a)) # *a = 튜플을 쪼개라 라는 의미, 리스트에서도 가능
```

## 튜플 딕셔너리
```python
for a in dict.items():
    print('{}의 나이는:{}'.format(a[0], a[1])
for a in dict.items():
    print('{}의 나이는:{}'.format(*a))
```
```python
ages = {'Tod':35, 'Jane':25,'Paul':14}
for a in ages.items():
    print('{}의 나이는 {}입니다'.format(*a))
# Tod의 나이는 35입니다.
# Jane의 나이는 25입니다.
# Paul의 나이는 14입니다.
```