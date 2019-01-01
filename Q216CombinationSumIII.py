class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k > 9:
            return 0
        if n >= k*9 or n <= k:
            return []
        if k == 1:
            return [[n]]
        results = []
        q = [[i] for i in range(1, 10)]
        while len(q):
            comb = q.pop(0)
            if len(comb) == k:
                if sum(comb) == n:
                    results.append(comb)
                continue
            max_ = max(comb)
            if max_ == 9:
                continue
            for j in range(max_+1, 10):
                q.append(comb+[j])
        return results