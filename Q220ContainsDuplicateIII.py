import bisect
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if k <= 0 or t < 0:
            return False
        visited = []
        i, j = 0, 1
        visited.append(nums[i])
        while j<len(nums):
            idx = bisect.bisect_left(visited, nums[j])
            if idx-1>=0 and abs(visited[idx-1]-nums[j]) <= t:
                return True
            if idx< len(visited) and abs(visited[idx]-nums[j]) <= t:
                return True
            visited.insert(idx, nums[j])
            if j-i >= k:
                idx = bisect.bisect_left(visited, nums[i])
                visited.pop(idx)
                i += 1
            j += 1
        return False
