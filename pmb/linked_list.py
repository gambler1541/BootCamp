class Node:
    def __init__(self, data=None):
        self.__data = data  # data 부분
        self.__next = None  # 다음 노드를 가리키는 참조 부분

    # 노드 삭제를 확인하기 위한 코드
    def __del__(self):
        print("data of {} is deleted".format(self.data))

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


class Linked_list:
    def __init__(self):
        # 연결 리스트의 첫 번째 노드를 가리킴
        self.head = None
        # 연결 리스트의 마지막 노드를 가리킴
        self.tail = None
        # 데이터의 개수
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        return False

    def size(self):
        return self.d_size

    # append()구현
    def append(self, data):
        # 삽입할 노드를 만듬
        new_node = Node(data)
        # 첫 번째 경우
        # 리스트가 비어 있을 때
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
        # 데이터가 한 개 이상 있을 때
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.d_size += 1

    def search_target(self, target, start=0):
        '''
        search_target(target, start=0) -> (data, pos)
        start로 target과 일치하는 첫 번째 데이터와 그 위치를 반환
        target이 존재하지 않을 때: -> (None, None)
        '''

        if self.empty():
            return None
        # 첫 번째 노드를 가리킨다
        pos = 0
        # 노드의 순회 코드
        cur = self.head
        # pos가 탐색 시작 위치 start보다 클 때만
        # 대상 데이터와 현재 노드의 데이터를 비교
        if pos >= start and target == cur.data:
            return cur.data, pos

        while cur.next:
            pos += 1
            # 노드의 순회 코드
            # cur이 노드의 next를 통해 다음 노드로 이동
            cur = cur.next

            # pos가 탐색 시작 위치 start보다 클 때만
            # 대상 데이터와 현재 노드의 데이터를 비교
            if pos >= start and target == cur.data:
                return cur.data, pos

        return None, None

    def search_pos(self, pos):
        """
        search_ps(pos) -> data
        pos가 범위를 벗어날 때 -> None
        """

        # pos는 0부터 시작
        # size는 1부터 시작(데이터가 있다는 가정)

        if pos > self.size() - 1:
            return None

        # pos를 대신해 순회하면서 증가하는 카운트
        # pos를 인자로 받았기 때문
        cnt = 0
        # cur를 맨 처음 값으로 지정
        cur = self.head
        # cnt 값과 pos가 같으면(0번째 데이터일 경우)
        if cnt == pos:
            # 해당 node의 data를 return
            return cur.data
        # cnt를 증가시키는 코드
        # cnt와 pos가 같아지면 순회를 멈춤
        while cnt < pos:
            cur = cur.next
            cnt += 1
        # cnt와 pos가 같아지면 그 data를 return
        return cur.data

    # remove()
    def remove(self, target):
        # data가 비었을 경우
        if self.empty():
            return None

        # before는 current 노드의 이전 노드를 가리킨다
        # 삭제할 때 요긴하게 쓰인다
        bef = self.head
        cur = self.head

        # A. 삭제 노드가 첫 번째 노드일 때
        if target == cur.data:
            if self.size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.d_size -= 1
            return cur.data

        while cur.next:
            bef = cur
            cur = cur.next
        # B. 삭제 노드가 첫 번째 노드가 아닐때
            if target == cur.data:
                if cur == self.tail:
                    self.tail = bef

                # B-2. 일반적인 경우
                bef.next = cur.next
                self.d_size -= 1
                return cur.data

        return None

def show_list(slist):
    if slist.empty():
        print('The list is empty')
        return

    for i in range(slist.size()):
        print(slist.search_pos(i), end="  ")


if __name__ == '__main__':
    '''
    위 예제는 하나의 데이터를 삽입, 삭제
    아래 예제는 여러개의 데이터 중 중간에 위치한 데이터ㅏ와 마지막 데이터를 삭제
    '''
    # slist = Linked_list()
    # print("데이터 개수: {}".format(slist.size()))
    # show_list(slist)
    # print()
    #
    #
    # slist.append(2)
    # print("데이터 개수: {}".format(slist.size()))
    # show_list(slist)
    # print()
    #
    # if slist.remove(2):
    #     print("데이터 개수: {}".format(slist.size()))
    #     show_list(slist)
    #     print()

    # 새객체 생성(실행될 때마다)
    # slist = Linked_list()
    # print("데이터 개수: {}".format(slist.size()))
    # show_list(slist)
    # print()
    #
    # slist.append(3)
    # slist.append(1)
    # slist.append(5)
    # slist.append(2)
    # slist.append(10)
    # slist.append(7)
    # slist.append(2)
    #
    # print("데이터 개수: {}".format(slist.size()))
    # show_list(slist)
    # print()
    #
    #
    # if slist.remove(2):
    #     print("데이터 개수: {}".format(slist.size()))
    #     show_list(slist)
    #     print()
    # else:
    #     print('target Not found')
    #
    # if slist.remove(2):
    #     print("데이터 개수: {}".format(slist.size()))
    #     show_list(slist)
    #     print()
    # else:
    #     print('target Not found')
    #


    slist = Linked_list()
    print(f'데이터 갯수 : {slist.size()}')
    show_list(slist)
    print()

    slist.append(3)
    slist.append(1)
    slist.append(5)
    slist.append(2)
    slist.append(10)
    slist.append(7)
    slist.append(2)

    print(f'데이터 갯수 : {slist.size()}')
    show_list(slist)
    print('\n')

    data1, pos1 = slist.search_target(2)
    if data1:
        print(f'searched data : {data1} at pos <{pos1}>')
    else:
        print('there is no such data')


    data2, pos2 = slist.search_target(2, pos1 + 1)
    if data2:
        print(f'searched data : {data2} at pos <{pos2}>')
    else:
        print('there is no such data')

