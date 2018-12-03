# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def minD(r):
            if r is None:
                return 0
            if r.left is None:
                if r.right is None:
                    return 1
                return 1 + minD(r.right)
            if r.right is None:
                return 1 + minD(r.left)
            return min(1 + minD(r.left), 1 + minD(r.right))

        return minD(root)