# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next

            odd, even = odd.next, even.next

        odd.next = even_head

        return head


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
s1.oddEvenList()