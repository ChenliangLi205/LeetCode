"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = [root]
        while len(queue):
            newQueue = []
            queue.append(None)
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
                if queue[i].left:
                    newQueue.append(queue[i].left)
                if queue[i].right:
                    newQueue.append(queue[i].right)
            queue = newQueue
        return root