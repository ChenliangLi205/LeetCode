import bisect
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return []
        if length == 1:
            return [0]
        enc = []
        results = [0]*length
        for i in range(length-1, -1, -1):
            idx = bisect.bisect_left(enc, nums[i])
            results[i] = idx
            enc.insert(idx, nums[i])
        return results