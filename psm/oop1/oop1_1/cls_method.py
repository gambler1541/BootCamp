class Person:
    # 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    # <name>_<age> 형태의 문자열을 인자로 받음
    def init_from_string(cls, string):
        '''
        string format : '<name>_<age>
        :param string:
        :return:
        '''
        name, age = string.split('_')
        # 인자로 받은것을 분석하고 일반적인 생성자를 다시 호출
        return cls(name, int(age))


if __name__ == '__main__':
    # 필요할 때마다 클래스 메서드를 호출해서 객체를 만들수 있음 
    p = Person.init_from_string('greg_30')
    print(p.name)
    print(p.age)