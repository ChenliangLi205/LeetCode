class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parents = []
        to_extend = [root]
        kids = []

        while True:
            for node in to_extend:
                if node.right is not None:
                    kids.append(node.right)
                if node.left is not None:
                    kids.append(node.left)
            parents.append(to_extend)
            to_extend = kids
            kids = []
            if len(to_extend) == 0:
                break
        labeled = []
        for i in range(len(parents)-1, -1, -1):
            for node in parents[i]:
                if node.left in labeled:
                    node.left = None
                if node.right in labeled:
                    node.right = None
            labeled = []
            for node in parents[i]:
                if node.val == 0 and node.left is None and node.right is None:
                    labeled.append(node)
                    node = None
        return root