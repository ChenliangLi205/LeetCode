class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        lenNums = len(nums)
        start, end, cnt = 0, nums[0], 1
        while end < lenNums-1:
            newEnd = end
            for i in range(start+1, end+1):
                newEnd = max(i+nums[i], newEnd)
            start = end
            end = newEnd
            cnt += 1
        return cnt