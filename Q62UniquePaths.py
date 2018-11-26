class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp = [[1]*m for _ in range(n)]
        row, col = 1, 1
        while row < n and col < m:
            for i in range(col, m):
                dp[row][i] = dp[row-1][i]+dp[row][i-1]
            for i in range(row+1, n):
                dp[i][col] = dp[i-1][col]+dp[i][col-1]
            row += 1
            col += 1
        return dp[-1][-1]