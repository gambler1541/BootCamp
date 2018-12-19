class Animal:
    def eat(self):
        # 모든 파생 클래스가 공통으로 가질 메서드인 eat()은 기본 클래스에 둔다
        print('eat something')


class Lion(Animal):
    def eat(self):
        print('eat meat')


class Deer(Animal):
    def eat(self):
        print('eat grass')


class Human(Animal):
    def eat(self):
        print('eat meat and grass')


if __name__ == '__main__':
    animals = []
    animals.append(Lion())
    animals.append(Deer())
    animals.append(Human())
    for animal in animals:
        # 다양성을 구현한 부분
        animal.eat()