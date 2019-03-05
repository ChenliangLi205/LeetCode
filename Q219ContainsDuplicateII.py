class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        if k == 0:
            return False
        p1, p2 = 0, 1
        numSet = set()
        numSet.add(nums[0])
        while p2 < len(nums):
            if p2 - p1 <= k:
                if nums[p2] in numSet:
                    return True
                numSet.add(nums[p2])
                p2 += 1
            else:
                numSet.remove(nums[p1])
                if nums[p2] in numSet:
                    return True
                numSet.add(nums[p2])
                p1 += 1
                p2 += 1
        return False