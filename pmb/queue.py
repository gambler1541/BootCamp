class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        if not self.head:
            return True
        return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.empty():
            self.head = new_node
            self.tail = new_node

            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

    def peek(self):
        if self.empty():
            return None

        return self.head.data



if __name__ == '__main__':
    q = Queue()

    print(q.empty())

    q.enqueue(1)
    print("delete data : {}".format(q.dequeue()))

    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue())


