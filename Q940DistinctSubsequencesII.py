class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        length = len(S)
        if length <= 2:
            return length
        char2loc = dict()
        dp = [0] * length
        dp[0] = 1
        char2loc[S[0]] = 0
        for i in range(1, length):
            char = S[i]
            dp[i] = dp[i - 1]
            if char not in char2loc:
                char2loc[char] = i
                dp[i] += dp[i - 1] + 1
            else:
                loc = char2loc[char]
                if loc != 0:
                    dp[i] += dp[i - 1] - dp[loc - 1]
                else:
                    dp[i] += dp[i - 1]
                char2loc[char] = i
        return dp[-1] % 1000000007
