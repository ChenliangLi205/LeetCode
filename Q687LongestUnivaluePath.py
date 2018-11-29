# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def noCurve(r):
            if r is None:
                return 0
            if r.left is None:
                if r.right is None:
                    return 0
                if r.val == r.right.val:
                    return 1 + noCurve(r.right)
                else:
                    return 0
            if r.right is None:
                if r.val == r.left.val:
                    return 1 + noCurve(r.left)
                else:
                    return 0
            if r.val == r.left.val:
                left = 1 + noCurve(r.left)
            else:
                left = 0
            if r.val == r.right.val:
                right = 1 + noCurve(r.right)
            else:
                right = 0
            return max(left, right)

        result = 0
        queue = [root]
        while queue:
            r = queue.pop(0)
            left, right = 0, 0
            if r.left:
                queue.append(r.left)
                if r.val == r.left.val:
                    left = 1 + noCurve(r.left)
            if r.right:
                queue.append(r.right)
                if r.val == r.right.val:
                    right = 1 + noCurve(r.right)
            result = max(result, left + right)
        return result
