class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        # (current length, copied length, steps)
        q = [(1, 1, 1)]
        min_steps = n
        while len(q):
            curLen, copied, steps = q.pop(-1)
            if steps >= min_steps:
                continue
            if curLen > n:
                continue
            if curLen == n:
                min_steps = min(min_steps, steps)
                continue

            q.append((curLen + copied, copied, steps + 1))
            if copied != curLen:
                q.append((curLen, curLen, steps + 1))
        return min_steps
