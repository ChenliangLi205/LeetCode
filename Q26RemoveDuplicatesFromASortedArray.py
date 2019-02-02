class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        cnt = 1
        for i in range(len(nums)-1):
            if nums[cnt] == nums[cnt-1]:
                nums.pop(cnt)
            else:
                cnt += 1
        return len(nums)