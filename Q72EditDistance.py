class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        len1, len2 = len(word1), len(word2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        for i in range(len2+1):
            dp[0][i] = i
        for i in range(len1+1):
            dp[i][0] = i
        row = 1
        while row <= len1:
            for col in range(1, len2+1):
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col]+1, dp[row][col-1]+1)
                else:
                    dp[row][col] = min(dp[row-1][col-1]+1, dp[row-1][col]+1, dp[row][col-1]+1)
            row += 1
        return dp[-1][-1]