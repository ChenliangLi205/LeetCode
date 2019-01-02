class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0
        dp = [0]*(amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(amount):
                if i + c > amount:
                    break
                dp[i+c] += dp[i]
        return dp[-1]