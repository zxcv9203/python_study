## 딕셔너리 만들기
+ 여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
+ 이름표를 이용하여 값을 꺼내 사용
+ 사용법
~~~ python
딕셔너리명 = {
  '이름표1':'값1',
  '이름표2':'값2'
}
~~~
~~~ python
wintable = {
  '가위' : '보',
  '바위' : '가위',
  '보' : '바위'
}
print(wintable['가위'] #  보   
~~~
 
## 딕셔너리 수정하기
> 추가  
list와 달리 index out of range 에러가 나지 않음  
```python
dict['three'] = 3
```
> 수정
```python
dict['one'] = 11
```
> 삭제
```python
del(dict['one'])
dict.pop('two')
```

## 딕셔너리와 반복문
+ 경우에 따라 가져올 값을 정할 수 있다.
```python
for key in ages.keys(): # keys() 생략 가능
  print(key)            #
```
```python
for value in ages.values():
  print(value)
```
+ 키와 value 둘다 가져올 수 있다.
```python
for key, value in ages.items():
  print('{}의 나이는 {}입니다'.format(key, value))
```
+ 딕셔너리는 순서를 지키지 않는다.
> 실습
```python
ages = {'Tod':35, 'Jane': 23, 'Paul':62}
for key in ages.keys(): # keys() 생략 가능  
    print(key)          # Tod, Jane, Paul이 출력 됨  
for value in ages.values():
    print(value)        # 62, 23, 35가 출력 됨  
```

 ## 리스트와 비교
 + 공통점

 1 | 2 | 3
---|---|---
one|two|three


