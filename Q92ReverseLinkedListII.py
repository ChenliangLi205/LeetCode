# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if head is None:
            return head
        if head.next is None:
            return head
        seg = []
        lastNode, currNode = None, head
        Left, Right = None, None
        cnt = 1
        while currNode:
            if n >= cnt >= m:
                seg.append(currNode)
                if cnt == m:
                    Left = lastNode
                if cnt == n:
                    Right = currNode.next
            if cnt > n:
                break
            lastNode = currNode
            currNode = currNode.next
            cnt += 1
        if Left is None:
            head = seg[-1]
        else:
            Left.next = seg[-1]
        for i in range(len(seg)-1, 0, -1):
            seg[i].next = seg[i-1]
        seg[0].next = Right
        return head