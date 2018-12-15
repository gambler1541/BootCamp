from binary_tree import *

class BST:
    '''
    이진 트리와 동일(상속 받지 않고 구현)
    '''
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, f):
        if not cur:
            return

        f(cur.data)
        self.preorder_traverse(cur.left, f)
        self.preorder_traverse(cur.right, f)


    def insert(self, data):
        # 삽입할 노드 생성 및 데이터 설정
        new_node = TreeNode()
        new_node.data = data

        cur = self.root

        # 루트 노드가 없을 때
        if cur == None:
            self.root = new_node
            return

        # 삽입할 노드의 위치를 찾아 삽입
        while True:
            # parent는 현재 순회 중인 노드의 부모 노드를 가리킴
            parent = cur
            # 삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < cur.data:
                cur = cur.left
                # 왼쪽 서브 트리가 None이면 새 노드를 위치시킨다
                if not cur:
                    parent.left = new_node
                    return
            # 삽입할 데이터가 현재 노드 데이터보다 클 때
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return

    def search(self, target):
        cur = self.root

        while cur:
            # 대상 데이터를 찾으면 데이터를 반환
            if target == cur.data:
                return cur
            # 대상 데이터가 노드 데이터보다 작으면
            # 왼쪽으로 이동
            elif target < cur.data:
                cur = cur.left
            # 대상 데이터가 노드 데이터보다 크면
            elif target > cur.data:
            # 오른쪽으로 이동
                cur = cur.right
        # while문을 빠져나온 경우
        # 대상 데이터가 트리안에 없다
        return cur

