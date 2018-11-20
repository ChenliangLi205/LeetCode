class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        cur = 0
        target = len(nums)
        visited = set()
        while cur > -1:
            if cur in visited or cur + nums[cur] in visited:
                cur -= 1
                continue
            if cur + nums[cur] >= target - 1:
                return True
            visited.add(cur)
            cur = cur + nums[cur]
        return False
