## 변수(Variable)

**데이터를 저장할 수 있는 메모리 공간 자체를 의미**

**변수 안에는 숫자, 문자, 객체, 함수 등을 담을 수 있다.**

### # 변수의 선언


C 언어에서는 변수를 할당한다면

```python
int num = 5;
```

그러나 파이썬에서 int 5의 값을 할당한다면 아래와 같이 나온다.

```python
num = 5
```


### # 변수는 값을 가지고 있지 않고 메모리 값을 참조한다.

```python
num1 = 100

num2 = num1

id(num1) #4526882416
id(num2) #4526882416
```

위와 같이 변수를 할당하면 num1과 num2는 같은 값을 가지고 있음을 알 수 있지만 현재까지는 num1의 값을 num2가 저장했을 수 있다고 생각할 수 있다.

여기에서 num_a 의 값을 변경하게 되면 num_a 의 값과 참조하는 메모리 주소도 변경되지만 num_b 는 최초에 참조했던 100의 메모리 주소를 그대로 가지고 있다.

```python
num_a # 200

id(num1) #4526885616

num_b # 100

id(num2) #4526882416
```

