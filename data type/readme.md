## format
### 문자열.format  
문자열에 포함된 대괄호의 개수보다 format안에 들어 있는 값의 수가 많으면 정상동작, 적으면 에러  
사용법
~~~python  
number = 20  
welcome = '환영'  
base = '{}번 손님{}'  

print(number, '번 손님', welcome) # 20번 손님 환영
print(base.format(number, welcome)) # 20번 손님 환영
print('{} 번 손님{}'.format(number, welcome) # 20번 손님 환영
~~~

## 문자열
### '또는 "로 문자열 만들기
'로 감싼 문자열안에는 "를 쓸 수 있고, "로 감싼 문자열에는 '를 쓸 수 있다.  
~~~python
string1 = '따옴표로 싼 문자열 안에는 큰따옴표를 사용할 수 있다.'
string2 = "큰따옴표로 싼 문자열안에는 따옴표를 사용할 수 있다."
~~~
### 따옴표/큰 따옴표 3개로 문자열 만들기
줄바꿈도 인식가능, 따옴표와 큰 따옴표를 섞어 쓸 수 있다.  
~~~python
string3 = """줄도 바꾸고
큰 따옴표와" 따옴표'를 마음대로 쓸 수 있음"""
~~~

## 정수와 실수
### 정수
정수끼리 더하거나 빼거나 곱하면 정수  
정수끼리 나누면 실수가 나올 수 있으나, 나눗셈의 몫만 구하려면 //연산자를 사용  
~~~python
a = 5//3 # 계산결과 1
~~~
### 실수
부동 소수점이라는 표현법을 이용해 소수점을 표시할 수 있는 숫자
정수를 실수로 바꾸려면 float를 사용
~~~python
a = float(5)
~~~

## 사용자 입력 받기
### input()
* 사용자의 키보드 입력을 return
~~~python
print('가위 바위 보 중 하나를 내주세요> ', end=' ')
mine = input()
print('mine:', mine)
~~~
* 간단한 print기능을 내장
~~~python
mine = input('가위 바위 보 중 하나를 내주세요> ')
print('mine:', mine)
~~~
### ctrl+c 프로그램 즉시 종료

