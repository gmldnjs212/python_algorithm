# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None

        dummy = ListNode(-200)
        dummy.next = l1
        prev_l1 = dummy

        while l1 and l2:
            if l2.val < l1.val:
                temp = prev_l1.next
                prev_l1.next = l2

                next_l2 = l2.next
                l2.next = temp

                prev_l1 = l2
                l2 = next_l2

            else:
                prev_l1 = l1
                l1 = l1.next

        if l1 is None:
            prev_l1.next = l2

        return dummy.next