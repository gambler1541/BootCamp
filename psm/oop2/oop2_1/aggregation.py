class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print('bang bang!')


class Police:
    def __init__(self):
        # police 객체가 만들어질 때 아직 Gun 객체를 가지고 있지 않음
        self.gun = None

    # acquire_gun 메서드를 통해 gun 을 가지게된다.
    def acquire_gun(self, gun):
        self.gun = gun

    # release_gun 메서드를 통해 가지고 있던 총을 반납할수 있음
    def release_gun(self):
        gun = self.gun
        self.gun = None
        return gun

    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print('Unable to shoot')


if __name__ == '__main__':
    # 경찰 객체가 생성될 때는 총을 가지고 있지 않음
    p1 = Police()
    print('p1 shoots')
    p1.shoot()
    print('')

    # p1 은 아직 총을 소유하지 않음.
    revolver = Gun('Revolver')
    # p1 이 revolver를 획득
    # acquire_gun 메서드를 통해 총을 얻고 나서야 총을 쏠수 있음
    p1.acquire_gun(revolver)
    # 이제 p1 이 총을 소유하므로
    # revolver는 None이 된다.
    revolver = None
    print('p1 shoots again')
    p1.shoot()
    print('')

    # p1 이 총을 반납했으므로
    # 더이상 총을 소유하지 않음
    # release_gun 메서드를 통해 총을 반납하므로 더이상 쏠수없음
    revolver = p1.release_gun()
    print('p1 shoots again')
    p1.shoot()