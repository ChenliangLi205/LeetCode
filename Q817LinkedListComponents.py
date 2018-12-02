# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        if head is None:
            return 0
        G = set(G)
        cur = head
        con = False
        blocks = 0
        while cur:
            if con:
                if cur.val not in G:
                    con = False
            else:
                if cur.val in G:
                    con = True
                    blocks += 1
            cur = cur.next
        return blocks