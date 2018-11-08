class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        numSet = set(nums)
        n = 1
        while n in numSet:
            n += 1
        return n