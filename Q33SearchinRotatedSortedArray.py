class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left, right = 0, len(nums)-1
        while right>left:
            if target == nums[right]:
                return right
            if target == nums[left]:
                return left
            if nums[left] > target > nums[right]:
                return -1
            if target > nums[left]:
                if nums[left+1] < nums[left]:
                    return -1
                left += 1
                continue
            if target < nums[right]:
                if nums[right-1] > nums[right]:
                    return -1
                right -= 1
                continue
        return -1