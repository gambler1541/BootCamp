# 추상 메서드 모듈 불러오기
from abc import *


# 파이썬 문법이라 생각하고 넘김
class Animal(metaclass = ABCMeta):
    @abstractmethod
    # 추상 메서드로 만들고 싶은 메서드 위에 데코레이터 @abstractmethod 를 붙여줌
    def eat(self):
        # 메서드 구현부를 pass로 해야 함수 몸체를 비워 두면 eat() 메서드는 추상 메서드가 된다.
        pass

a = Animal()