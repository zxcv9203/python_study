## format
문자열.format  
문자열에 포함된 대괄호의 개수보다 format안에 들어 있는 값의 수가 많으면 정상동작, 적으면 에러  
사용법
~~~python  
number = 20  
welcome = '환영'  
base = '{}번 손님{}'  

print(number, '번 손님', welcome)
print(base.format(number, welcome))
print('{} 번 손님{}'.format(number, welcome)
