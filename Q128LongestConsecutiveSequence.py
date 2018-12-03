class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        length = 0
        curLen = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                curLen += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                length = max(curLen, length)
                curLen = 1
        length = max(curLen, length)
        return length