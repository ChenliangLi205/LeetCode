# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        oneLevel = [root]
        ans = []
        while len(oneLevel) > 0:
            ans.append(oneLevel[-1].val)
            newLevel = []
            for node in oneLevel:
                if node.left is not None:
                    newLevel.append(node.left)
                if node.right is not None:
                    newLevel.append(node.right)
            oneLevel = newLevel
        return ans
        