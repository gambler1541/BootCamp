class Account:
    def __init__(self, name, money):
        self.user = name
        # 인스턴스 멤버 선언이 아니라 setter 메서드를 호출
        self.balance = money

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, money):
        if money < 0:
            return

        # 실제 인스턴스 멤버 선언이 일어나는 부분
        self._balance = money


if __name__ == '__main__':
    my_acnt = Account('greg', 5000)
    # setter 함수를 통해 변경을 시도하므로 _balance 메버의 값은 음수로 변경되지 않음
    # 음수로 변경되지 않았으므로 실행 결과는 5000이 나옴
    my_acnt.balance =- 3000
    # getter 함수인 balance() 메서드를 호출해 _balance apaqjdp wjqrms,
    print(my_acnt.balance)
