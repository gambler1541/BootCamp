### 프로그래밍의 패러다임

- 절차지향 프로그래밍
- 객체지향 프로그래밍
- 함수형 프로그래밍


### 절차지향프로그래밍

- 어떤일을 수행하는 긴 코드를 기능별로 나누고 함수로 정의
- 함수 호출을 사용해 코드를 작성
- 쉽게 프로그램을 이해하고 유지 보수가 쉽다

### 객체지향 프로그래밍

- 변수와 함수를 가진 객체를 이용하는 패러다임

### 캡슐화

- 변수(데이터)와 함수를 하나의 단위(클래스)로 묶는 것

```python
# pseudo_class.py

def person_init(name, money):
	obj = {'name': name, 'money': money}
	obj['give_money'] = Person[1]
	obj['get_money'] = Person[2]
	obj['show'] = Person[3]
	return obj
	
def give_money(self, other, money):
	self['money'] -= money
	other['get_money'](other, money)
	
def get_money(self, money):
	self['money'] += money
	
def show(self):
	print('{} : {}'.format(self['name'], self['money']	


if __name__=='__main__':
	# Person[0]에 2개의 객체(g, j) 생성
	g = Person[0]('greg', 5000)
	j = Person[0]('john', 2000)
	
	g['show'](g)
	j['show'](j)
	
	print('')
	
	g['give_money'](g, j, 2000)
	
	g['show'](g)
	j['show'](j)
	
>> greg : 5000
>> john : 2000
>> 
>> greg : 3000
>> john : 2000	

```

### 메시지 패싱

서로 다른 객체가 함수 호출을 통해 상호작용하여 객체의 상태(데이터)가 변하는 것

1) 서로 다른 객체가 상호작용일 때 함수를 호출

2) 함수 안에서 상대의 변수(데이터)를 바꾸려면 상대가 가진 특정함수를 호출

## property 와 private 속성

**private 속성**

```python
class Account:
	def __init__(self, name, money):
		self.name = name
		self.balance = money
		
	def get_balance(self):
		return self.__balance
		
	def set_balance(self, money):
		if money < 0:
			return
		self.__balance = money


my_acnt = Account('greg', 5000)
my_acnt.__balance = -3000
my_acnt.balance
>> 5000

my_acnt.__dict__
>> {'name': 'greg', 'balance': 5000, '__balance': -3000}

# __balance 라는 인스턴스 메서드가 새로 생성
```


```python
class Account:
	def __init__(self, name, money):
		self.name = name
		self.balance = money
		
	@property
	def balance(self):
		return self._balance
		
	@balance.setter
	def balance(self, money):
		if money < 0:
			return
		self._balance = money
		
my_acnt = Account('greg', 5000)
my_acnt.balance = -3000
my_acnt.balance
>> 5000

my_acnt.__dict__
>> {'user': 'greg', '_balance': 5000}

```

1) `property` 는 `get_balance` 메서드와 같은 역할을 한다.

2) 인스턴스에 접근하여 값을 변경하더라도 메서드가 새로 생성이 될 뿐 인스턴스의 메서드를 새로 재정의 할 수 없다.

