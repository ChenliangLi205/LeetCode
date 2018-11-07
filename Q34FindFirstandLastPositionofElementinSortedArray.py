class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if target == nums[0]:
                return [0, 0]
            else:
                return [-1, -1]
        left, right = 0, len(nums)-1
        while right >= left:
            if target > nums[right]:
                return [-1, -1]
            if target < nums[left]:
                return [-1, -1]
            if target > nums[left]:
                left += 1
            if target < nums[right]:
                right -= 1
            if target == nums[left] == nums[right]:
                return [left, right]
        return [-1, -1]