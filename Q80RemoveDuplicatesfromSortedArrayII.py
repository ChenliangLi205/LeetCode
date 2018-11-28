class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        dup, cur = False, 1
        while cur < len(nums):
            if dup and nums[cur] == nums[cur-1]:
                nums.pop(cur)
                cur -= 1
            elif nums[cur] == nums[cur-1]:
                dup = True
            else:
                dup = False
            cur += 1
        return len(nums)