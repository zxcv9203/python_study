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
