# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        arr = []

        # head가 비어있는 경우 True ( 조건에 있음 )
        if not head:
            return True

        # head에 값이 있다면 모든값을 arr에 넣는다.
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next

        # 하나 이상 남았을 때, 맨앞과 맨뒤의 요소를 꺼낸다. > 한번이라도 다르면 False
        while len(arr) > 1:
            # arr.pop(0) = 맨 앞의 요소를 꺼냄, 0이 없으면 맨 뒤부터 꺼냄
            if arr.pop(0) != arr.pop():
                return False
        return True
