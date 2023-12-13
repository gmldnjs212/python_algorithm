# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# 리스트를 단일 연결 리스트로 변환
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 단일 연결 리스트를 리스트로 변환
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

s1 = Solution()
head_list = [1, 2, 3, 4, 5]

# 리스트를 단일 연결 리스트로 변환
head_linkedlist = list_to_linkedlist(head_list)

# reverseList 메서드 호출
reversed_linkedlist = s1.reverseList(head_linkedlist)

# 결과를 리스트로 변환하여 출력
result_list = linkedlist_to_list(reversed_linkedlist)
print(result_list)
