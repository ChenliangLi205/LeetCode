class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if sum(nums) < s:
            return 0
        p1 = 0
        p2 = 1
        currSum = sum(nums[p1:p2])
        minLen = len(nums)
        while p2 <= len(nums):
            if currSum >= s:
                minLen = min(minLen, p2-p1)
                if p2 - p1 == 1:
                    return minLen
                else:
                    currSum -= nums[p1]
                    p1 += 1
            else:
                if p2 < len(nums):
                    currSum += nums[p2]
                p2 += 1
        return minLen