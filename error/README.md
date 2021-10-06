# 에러처리

파이썬으로 프로그래밍을 하다보면 다양한 에러가 발생합니다.

예를들어, 다음과 같은 상황이 있습니다.

``` python
list = []
list[0]
#out of range
```

위와 같은 코드를 실행시켜보면 다음과 같은 에러가 발생합니다.

`IndexError: list index out of range`

이런 에러가 발생할 때 프로그래머가 직접 처리하게 할수 도 있습니다.

## try except

try except 구문을 사용하면 특정 에러가 발생했을 때 동작을 직접 지정할 수 있습니다.

다음 예제를 봅시다.

``` python
list = []
try:
    print(list[0])
except IndexError:
    print("리스트의 범위를 넘어갔습니다.")
```

다음코드를 실행시켜보면 out of range라는 index error가 아닌 직접 작성한 "리스트의 범위가 넘어갔습니다."라는 문장이 실행됩니다.

다음과 같이 try except를 사용하면 특정 에러에 대해 개발자가 직접 동작을 지정해줄 수 있습니다.

```python
try:
	#에러가 발생할 가능성이 있는 코드
except Exception: # Exception은 에러 종류를 적으면 됩니다. (ex: IndexError)
	# 에러가 발생 했을 경우 처리할 코드
```

만약에러가 발생하지 않을경우 try문이 실행됩니다.

다음 코드를 실행시켜보면 정상적일때는 try 블럭에 있는 코드를 실행 하고 에러가 발생할 경우 except 블럭에 있는 동작을 합니다.

``` python
def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print("{}번째 index의 값을 가져올 수 없습니다.".format(index))

list1 = [1, 2, 3]
safe_pop_print(list1, 2)
safe_pop_print(list1, 5)
```

물론 다음과 같은 방식으로 if else 구문으로도 에러처리를 할 수 있습니다.

``` python
def safe_pop_print(list, index):
    if index < len(list):
        print(list.pop(index))
    else :
        print("{}번째 index의 값을 가져올 수 없습니다.".format(index))
```

두 방법중에 더 간단하게 구현되는 방식을 선택해서 사용하면 됩니다.

만약 양쪽의 구현되는 난이도가 비슷하다면 if else 구문을 사용하는 것이 더 좋습니다.

예를 들어, 다음과 같은 상황일 경우 if else문으로는 구현하기 어렵기 때문에 try except 구문을 사용하는 것이 좋습니다.

``` python
try:
    import my_module
except ImportError:
    print("모듈이 없습니다.")
```

## 예외의 이름을 모르는 경우

만약 try except 구문을 사용할 때 어떤 에러가 발생한지 모르는 경우가 있을 것입니다.

예를들어, 하나의 try 구문에 여러가지 코드가 존재할 경우 다음과 같이 작성하여 처리할 수 있습니다.

``` python
try:
    list = []
    print(list[0])
    text = "abc"
    number = int(text)
except:
    print("에러가 발생했습니다.")
```

위와같이 except만 사용하면 에러 발생시 except에서 처리하게 됩니다.

하지만 except만 적어서 처리할 경우 어떤 에러가 발생했는지 알 수 없습니다.

그래서 다음과 같은 방법으로 에러를 처리할 수 있습니다.

``` python
try:
    list = []
    print(list[0])
    text = "abc"
    number = int(text)
except Exception as ex:
    print("에러가 발생했습니다.", ex)
```

except에 Exception as ex를 추가하면 발생한 에러를 확인할 수 있습니다.

여기서 ex는 발생한 에러 메시지가 담기는 변수로 어떤 이름을 사용해도 괜찮습니다.

## raise

프로그래밍을 할 때 특정상황에서 프로그래머가 직접 에러를 발생시켜야 하는 경우도 있습니다.

예를들어, 특정 값을 받아야 하는데 잘못된 값이 들어왔을 경우 에러가 발생해야 한다고 합시다.

다음 예제를 살펴보겠습니다.

``` python
def rsp(mine, yours):
    allowed = ["가위", "바위", "보"]
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
    # 가위바위보 승패를 판단하는 코드

try:
    rsp("가위", "바")
except ValueError:
    print("잘못된 값이 입력되었습니다.")
```

잘못된 값이 들어오면 raise 구문을 이용하여 위와 같이 에러를 발생시킬 수 있습니다.

다음과 같이 raise를 이용하여 반복문을 종료할수도 있습니다.

``` python
school = {"1반" : [172, 175, 188, 199], "2반": [188,156,176]}
try:
	for class_number, students in school.items():
		for student in students:
			if student > 190:
				print(class_number, "에 190을 넘는 학생이 있습니다.")
				raise StopIteration
except StopIteration:
    print("정상종료")
```

위의 코드는 StopIteration 예외를 발생시켜 try 구문이 정상종료 되었음을 알려줍니다.

raise는 유용하게 쓰일수 있지만 너무 많이 사용하면 코드를 읽기 어려워지므로 꼭 필요한 상황에만 사용하는 것이 좋습니다.