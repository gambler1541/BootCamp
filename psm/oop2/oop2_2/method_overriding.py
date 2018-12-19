class CarOwner:
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        print('{} can not do anything else'.format(self.name))

    # 나머지 메서드


class Car:
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)

    def drive(self):
        # 차 주인이 운전외에 아무것도 하지못함
        self.owner.concentrate()
        # 차 주인이 현재 운전하는 상태임을 나타
        print('{} is drving now.'.format(self.owner.name))

    # 나머지 메서드


class SelfDrivingCar(Car):
    # drive 메서드만 클래스 안에서 다시 정의
    # 파생 클래스에서 상속받은 메서드를 다시 구현하는 것을 메서드 오버라이딩이라한다.
    def drive(self):
        # 차가 직접 운전하고 잇는 상태를 나타냄
        print('Car is driving by itself')


if __name__ == '__main__':
    car = Car('Greg')
    # car.drive 는 Car 객체가 drive() 메서드를 호출함
    car.drive()
    print('')

    s_car = SelfDrivingCar('John')
    # s_car.drive 는 SelfDrivingCar 객체가 drive() 메서드를 호출함
    s_car.drive()