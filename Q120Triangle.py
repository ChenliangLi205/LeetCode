class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        dp = [[0]*(i+1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0]+triangle[i][0]
            dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
        return min(dp[-1])