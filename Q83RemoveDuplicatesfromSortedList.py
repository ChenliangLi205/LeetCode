# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        last, cur = head, head.next
        while cur:
            if cur.val == last.val:
                last.next = cur.next
                cur = cur.next
            else:
                last = cur
                cur = cur.next
        return head