# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if head is None:
            return head
        if head.next is None:
            return head
        lastNode, currNode = None, head
        parNodeLeft, parNodeRight = None, None
        parFound = False
        while currNode:
            if parFound:
                if currNode.val < x:
                    nextNode = currNode.next
                    lastNode.next = currNode.next
                    currNode.next = parNodeRight
                    if parNodeLeft is not None:
                        parNodeLeft.next = currNode
                    else:
                        head = currNode
                    parNodeLeft = currNode
                    currNode = nextNode
                else:
                    lastNode = currNode
                    currNode = currNode.next
            else:
                if currNode.val >= x:
                    parNodeLeft = lastNode
                    parNodeRight = currNode
                    parFound = True
                lastNode = currNode
                currNode = currNode.next
        return head