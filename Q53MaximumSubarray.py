class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        soFar = 0
        result = nums[0]
        for i in range(len(nums)):
            soFar = max(0,soFar)+nums[i]
            result = max(result, soFar)
        return result