class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if(nums[-1] > nums[0]):
            return nums[0]
        if(nums[-1] < nums[-2]):
            return nums[-1]
        lastPtr = len(nums)-1
        firstPtr = 0
        while(lastPtr >= firstPtr):
            if(nums[firstPtr] > nums[firstPtr+1]):
                return nums[firstPtr+1]
            if(nums[lastPtr] < nums[lastPtr-1]):
                return nums[lastPtr]
            lastPtr -= 1
            firstPtr += 1
        return nums[lastPtr]