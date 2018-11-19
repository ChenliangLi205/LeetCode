# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxVal = -1000000

    def maxPathSum(self, root):
        self.maxSum(root)
        return self.maxVal

    def maxSum(self, r):
        if r.left is None and r.right is None:
            self.maxVal = max(self.maxVal, r.val)
            return r.val
        if r.left is None:
            maxRight = self.maxSum(r.right)
            self.maxVal = max(r.val + maxRight, r.val, self.maxVal)
            return max(maxRight + r.val, r.val)
        if r.right is None:
            maxLeft = self.maxSum(r.left)
            self.maxVal = max(r.val + maxLeft, r.val, self.maxVal)
            return max(maxLeft + r.val, r.val)
        maxLeft, maxRight = self.maxSum(r.left), self.maxSum(r.right)
        self.maxVal = max(r.val, r.val + maxLeft, r.val + maxRight, r.val + maxLeft + maxRight, self.maxVal)
        return max(maxLeft + r.val, maxRight + r.val, r.val)