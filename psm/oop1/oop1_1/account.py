class Account:
    # 클래스 멤버
    num_acnt = 0

    @classmethod
    # 클래스 멤버를 반환하는 클래스 메서드 정의
    def get_num_acnt(cls):
        '''
        cls.get_num_acnt() -> integer
        :return:
        '''
        return cls.num_acnt

    def __init__(self, name, money):
        # 생성자 안에있는 self.name, self.balance 는 객체마다 다른 값을 가지는 인스턴스 멤버
        self.user = name
        self.balance = money
        # 객체를 생성할 때마다 클래스 멤버인 계좌 수를 하나씩 늘려줌
        Account.num_acnt += 1

    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    # transfer() 메서드는 메시지 패싱을 하는 함수
    def transfer(self, other, money):
        '''
        obj.transfer(other, money) -> bool
        other : The object to interact with
        money : money the user wants to send

        returns True if the balance is enough to transfer
        returns False not
        :param other:
        :param money:
        :return:
        '''
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False

    # __str__() 메서드는 파이썬 예약함수
    def __str__(self):
        return 'user: {}, balance: {}'.format(self.user, self.balance)


if __name__ == '__main__':
    # 객체 생성
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    # 생성 확인
    print('object created')
    print(my_acnt)
    print(your_acnt)
    print()

    # 인스턴스 메서드 호출하는 방법
    # 1. by object

    my_acnt.deposit(500)

    # 2. by class
    # Account.deposit(my_acnt, 500)

    # deposit 확인
    print('deposit')
    print(my_acnt)
    print()

    # withdraw 함수 사용법
    print('withdraw')
    money = my_acnt.withdraw(1500)
    if money:
        print('withdraw money:{}'.format(money))
    else:
        print('Not enough to withdraw')
    print()

    # 클래스 멤버에 접근하는 방법
    print('class member')
    # 1. by class
    print(Account.num_acnt)
    # 2. by object
    # print(my_acnt.num_anct)
    print()

    # 클래스 메서드를 호출하는 방법
    print('class method')
    # 1.by class
    n_acnt = Account.get_num_acnt()
    # 2. by object
    # n_acnt = my_acnt.get_num_acnt()

    print('The number of accounts: {}'.format(n_acnt))
    print()

    # 메시지 패싱
    print('message passing')
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)