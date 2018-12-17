class A:
    # 클래스 멤버
    c_mem = 10

    # 데코레이터 클레스메서드
    @classmethod
    def cls_f(cls):
        print(cls.c_mem)

    def __init__(self, num):
        self.i_mem = num

    def ins_f(self):
        print(self.i_mem)

#
# if __name__ == '__main__':
#     # 객체가 없는 상태에서 클래스 이름을 통해 클래스 멤버 c_mem에 접근
#     print(A.c_mem)
#     # 클래스 메서드 cls_f를 호출
#     A.cls_f()

# 파이썬에서 전역 함수를 대체하려면 클래스 메서드보다 정적 메서드(static method)가 더 어울림.


if __name__ == '__main__':
    print(A.c_mem)
    A.cls_f()

    # 객체 생성
    a = A(20)
    # 객체를 토앻 클래스 멤버에 접근
    print(a.c_mem)
    # 객체를 통해 클래스 메서드를 호
    a.cls_f()
