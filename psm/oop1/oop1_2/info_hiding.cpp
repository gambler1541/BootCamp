class Account{
// public, protected, private 세종류의 접근 제어 지시자
public:
// 생성자: 파이썬 클래스의 __init__()과 같음
    Account(string name, init money){
        user = name;
        balance = money;
    }
    // 인스턴스 메서드(멤버 함수)
    int get_balance(){
        return balance;
    }
    // 인스턴스 메서드(멤버 함수)
    void set_balance(int money){
        if(money < 0){
            return
        }
        balance = money;
    }
private:
    // 인스턴스 멤버(멤버 변수)
    string user;
    int balance;
};

int main(void){
    Account my_acnt('greg', 5000);
    // my_acnt라는 객체를 생성한 다음 객체를 사용해 balance 멤버에 접근
//    my_acnt.balance;
    my_acnt.set_balance(-3000);
    cout << my_acnt.get_balance() << endl;

    return 0;
}