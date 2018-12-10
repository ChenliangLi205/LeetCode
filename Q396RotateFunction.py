class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length == 0:
            return 0
        if length == 1:
            return 0
        if length == 2:
            return min(A)
        sum_ = sum(A)
        prevSum = 0
        for i in range(length):
            prevSum += i*A[i]
        max_ = prevSum
        for j in range(1, length):
            curSum = prevSum - sum_ + length*A[j-1]
            max_ = max(max_, curSum)
            prevSum = curSum
        return max_