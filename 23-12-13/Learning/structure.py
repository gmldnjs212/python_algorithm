# https://velog.io/@king3456/Python-%EC%9C%BC%EB%A1%9C-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-4-%EB%A7%81%ED%81%AC%EB%93%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8-Linked-List

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    # 삽입 구현
    def __init__(self):
        # 링크드 리스트의 첫 번째 노드를 가리키는 포인터인 head를
        # 초기에는 아무 것도 가리키지 않도록 설정하는 것을 의미
        self.head = None

    def append(self, val):
        # self.head가 없다면 , 생성만 된 연결리스트라면
        if not self.head:
            # head를 val값으로 지정하고 다음요소는 None으로 설정
            self.head = ListNode(val, None)
            return

        # 현재 바라보고 있는 노드를 head로 설정한다.
        node = self.head
        # while문을 통해 맨 마지막 노드까지 이동한다.
        while node.next:
            node = node.next
        # 맨마지막 노드 다음에 val을 추가한다.
        node.next = ListNode(val, None)

lst = [1,2,3]
l1 = LinkedList()
for e in lst:
    l1.append(e)