class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) <= 2:
            return len(tree)
        baskets = []
        maxLen = 0
        curLen = 0
        for i in range(len(tree)-1, -1, -1):
            if tree[i] in baskets:
                curLen += 1
            elif len(baskets) < 2:
                baskets.append(tree[i])
                curLen += 1
            elif len(baskets) == 2:
                baskets = [tree[i]]
                baskets.append(tree[i+1])
                curLen = 2
                for j in range(i+2, len(tree)):
                    if tree[j] != baskets[-1]:
                        break
                    else:
                        curLen += 1
            maxLen = max(maxLen, curLen)
        return maxLen