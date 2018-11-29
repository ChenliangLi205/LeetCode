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
        cur, last = head, None
        dup = False
        while cur:
            if dup:
                nex = cur.next
                if last:
                    last.next = nex
                else:
                    head = nex
                if nex is None:
                    break
                if nex.val != cur.val:
                    dup = False
                cur = nex
            else:
                nex = cur.next
                if nex is None:
                    break
                if nex.val == cur.val:
                    dup = True
                    if last:
                        last.next = nex
                    else:
                        head = nex
                    cur = nex
                else:
                    last = cur
                    cur = nex
        return head
