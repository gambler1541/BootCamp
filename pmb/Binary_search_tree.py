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


    def __remove_recursion(self, cur, target):
        #탈출 조건1
        # 타겟이 트리 안에 없을 경우
        if cur == None:
            return None, None

        #대상 데이터가 노트 데이터보다 작으면
        # 노드의 왼쪽 자식에서 대상 데이터를 가진 노드를 지운다(재귀 함수)
        elif target < cur.data:
            cur.left, rem_node = self.__remove_recursion(cur.left, target)
        #대상 데이터가 노드 데이터보다 크면
        # 노드의 오른쪽 자식에서 대상 데이터를 가진 노드를 지운다(재귀 함수)
        elif target > cur.data:
            cur.right, rem_node = self.__remove_recursion(cur.right, target)

        #탈출 조건2
        # target == cur.data
        else:
        # 1. 리프 노드일 때
            if not cur.left and cur.right:
                rem_node = cur
                cur = None
        # 2-1. 자식 노드가 하나일 때, 왼쪽 자식이 있을 때
            elif not cur.right:
                rem_node = cur
                cur = cur.left
        # 2-2. 자식 노드가 하나일 때, 오른쪽 자식이 있을 때
            elif not cur.left:
                rem_node = cur
                cur = cur.right
        # 3. 자식 노드가 두 개일 때
            else:
        # 4. 대체 노드를 찾음
                replace = cur.left
                while replace.right:
                    replace = cur.right
            # 5. 삭제 노드와 대체 노드의 값을 교환
                cur.data, replace.data = replace.data, cur.data
            # 6. 대체 노드를 삭제하면서 삭제된 노드를 받아옴(재귀 함수)
                cur.left, rem_node = self.__remove_recursion(cur.left, replace.data)
        # 삭제 노드가 루트 노드일 경우
        # 루트가 변경될 수 있기 때문에
        # 삭제 후 현재 루트를 반환
        return cur,rem_node

    def remove(self,target):
        self.root, removed_node = self.__remove_recursion(self.root, target)
        removed_node.left = removed_node.right = None

        return removed_node


if __name__ == '__main__':
    bst = BST()

    # insert
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f = lambda x: print(x, end='  ')

    # 전위 순회
    bst.preorder_traverse(bst.get_root(), f)
    print()

    bst.remove(9)
    bst.preorder_traverse(bst.get_root(), f)

