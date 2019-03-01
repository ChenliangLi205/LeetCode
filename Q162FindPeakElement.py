class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        i = 0
        j = len(nums)-1
        if nums[i] > nums[i+1]:
            return i
        if nums[j] > nums[j-1]:
            return j
        i+=1
        j-=1
        while i<=j:
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i
            if nums[j]>nums[j-1] and nums[j] > nums[j+1]:
                return j
            i += 1
            j -= 1
        return 0