class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if min(nums) > target:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1;
        for i in range(1, target + 1):
            dp[i] = 0
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i - x]
        return dp[-1]
