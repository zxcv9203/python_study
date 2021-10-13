# 논리 연산과 if문 더 알아보기
## 논리 연산 더 알아보기
+   단락평가
    +   논리 연산에서 코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 더 보지 않고 값을 결정하는 것을 의미
    +   복잡한 코드를 단순하게 하는 방식
``` python
a = 10
if a < 10 and 2**a > 1000 and a%5==2 and round(a)==a:
    print('복잡한 식')
```
+   and 는 모두가 참이어야 실행되고, or 연산에서는 하나만 참이어도 실행된다.
    +   and의 조건중에 거짓이 있으면 바로 if문을 탈출한다.
``` python
print('TEST 1')
def return_false():
    print("함수 return false")
    return False
def return_true():
    print("함수 return true")
a = return_false()
b = return_true()
if a and b:
    print("TRUE")
else:
    print("FALSE")
# 실행결과
# 함수 return false
# 함수 return true
# FALSE
```

``` python 
print('TEST 2')
def return_false():
    print("함수 return false")
    return False
def return_true():
    print("함수 return true")
if return_false() and return_true():
    print("TRUE")
else:
    print("FALSE")
# 실행결과
# 함수 return false
# FALSE
```
## bool 값과 논리 연산
### True, False
+   숫자 0을 제외한 모든 수 = True
+   (빈 딕셔너리, 빈 리스트)를 제외한 (모든 딕셔너리, 리스트) = True
+   아무 값도 없다는 의미인 None = False
+   빈 문자열을 제외한 모든 문자열 = True
``` python
bool(0) # False
bool(1) # True
bool(-13515) # True
bool([]) # False
bool([3]) # False
bool(None) # False
bool('hi') # True
bool('') # False
```
+   A and B
    +   A가 False이면 B의 값은 검사하지 않고 결과는 A의 값인 True
    +   A가 True이면 B의 값에 따름
+   A or B
    +   A가 True이면 B의 값은 검사하지 않고 결과는 A의 값을 따름
    +   A가 False이면 B의 값에 따름
``` python
value = input('입력해주세요') or '아무것도 못 받았어'
print('입력 받은 값>', value)
# 실행 결과 
# (아무것도 입력하지 않았을 때) 입력 받은 값> 아무것도 못 받았어
# (1234 입력 했을 때) 입력 받은 값 > 1234
```
+   input()이 빈 경우 False이므로 / 뒤의 값은 문자열이므로 True라서 value는 '아무것도 못 받았어'가 된다.
+   input()이 있는 경우 True이므로 / 뒤는 더이상 보지 않고 value는 (입력받은 값)이 된다.