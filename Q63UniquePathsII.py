class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[-1][-1] == 1:
            return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*cols for _ in range(rows)]
        dp[0][0] = 1
        for i in range(1, cols):
            dp[0][i] = 0 if obstacleGrid[0][i-1] else dp[0][i-1]
        for i in range(1, rows):
            dp[i][0] = 0 if obstacleGrid[i-1][0] else dp[i-1][0]
        row, col = 1, 1
        while row < rows and col < cols:
            for i in range(col, cols):
                left = 0 if obstacleGrid[row][i-1] else dp[row][i-1]
                up = 0 if obstacleGrid[row-1][i] else dp[row-1][i]
                dp[row][i] = left + up
            for i in range(row, rows):
                left = 0 if obstacleGrid[i][col-1] else dp[i][col-1]
                up = 0 if obstacleGrid[i-1][col] else dp[i-1][col]
                dp[i][col] = left + up
            row += 1
            col += 1
        return dp[-1][-1]