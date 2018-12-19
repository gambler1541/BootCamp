# 채워진 다이아몬드 모양은 합성을 나타냄
# computer 가 cpu 를 소유하고 있다

class CPU:
    pass


class RAM:
    pass


class Computer:
    def __init__(self):
        # 생성자에서 CPU 객체를 생성아여 멤버 cpu 에 할당
        self.cpu = CPU()
        self.ram = RAM()