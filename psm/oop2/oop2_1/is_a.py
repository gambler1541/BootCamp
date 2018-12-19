class Computer:
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram

    def browse(self):
        print('browse')

    def work(self):
        print('work')


# Computer 를 상속함으로써 Computer 가 가지고 있는 모든 멤버와 메서드를 가짐
class Laptop(Computer):
    # 멤버 추가
    def __init__(self, cpu, ram, battery):
        super().__init__(cpu,ram)
        self.battery = battery

    # 메서드 추가
    def move(self, to):
        print('move to {}'.format(to))


if __name__ == '__main__':
    lap = Laptop('intel', 16, 'powerful')
    lap.browse()
    lap.work()
    lap.move('office')