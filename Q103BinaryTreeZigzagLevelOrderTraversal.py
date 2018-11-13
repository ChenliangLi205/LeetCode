# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        activeNodes = [root]
        results = []
        right2left = False
        while True:
            newActive = []
            subResults = []
            if not any(activeNodes):
                break
            for i in range(len(activeNodes)-1, -1, -1):
                if activeNodes[i] is not None:
                    subResults.append(activeNodes[i].val)
                    if right2left:
                        newActive.append(activeNodes[i].right)
                        newActive.append(activeNodes[i].left)
                    else:
                        newActive.append(activeNodes[i].left)
                        newActive.append(activeNodes[i].right)
            right2left = not right2left
            results.append(subResults)
            activeNodes = newActive
        return results