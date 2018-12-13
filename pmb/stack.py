class Node:
    def __init__(self, data=None):
        self.__data = data  # data 부분
        self.__next = None  # 다음 노드를 가리키는 참조 부분
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next

        return ret_data

    def empty(self):
        if not self.head:
            return True
        return False

    def peek(self):
        if self.empty():
            return None

        return self.head.data


if __name__ == '__main__':
    s = Stack()

    print(s.empty())

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(f'peek of data : {s.peek()}')

    while not s.empty():
        data = (s.pop())
        print(data, end = '  ')





