# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head

        prevs = [head]
        cur = head.next

        while cur is not None:
            inserted = False
            for i in range(len(prevs)):
                if prevs[i].val > cur.val:
                    prevs.insert(i, cur)
                    inserted = True
                    break
            if not inserted:
                prevs.append(cur)
            cur = cur.next

        head = prevs[0]
        cur = head
        for i in range(1, len(prevs)):
            cur.next = prevs[i]
            cur = cur.next
        cur.next = None
        return head