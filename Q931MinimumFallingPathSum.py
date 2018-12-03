class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows = len(A)
        if rows == 0:
            return 0
        cols = len(A[0])
        if cols == 0:
            return 0
        if rows == 1:
            return min(A[0])
        # dp[i][j] stores the minimum falling path sum for starting point i,j
        dp = [[0]*cols for _ in range(rows)]
        for j in range(cols):
            dp[-1][j] = A[-1][j]
        for i in range(rows-2, -1, -1):
            dp[i][0] = A[i][0]+min(dp[i+1][0], dp[i+1][1])
            dp[i][cols-1] = A[i][cols-1] + min(dp[i+1][cols-1], dp[i+1][cols-2])
            for j in range(1, cols-1):
                dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])
        return min(dp[0])
