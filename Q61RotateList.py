# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        length, cur, tail = 0, head, None
        while cur is not None:
            length += 1
            tail = cur
            cur = cur.next
        if k % length == 0:
            return head
        k %= length
        target = length - k
        oldHead = head
        cur, cnt = head, 1
        while cnt != target:
            cnt += 1
            cur = cur.next
        newHead = cur.next
        cur.next = None
        head = newHead
        tail.next = oldHead
        return head