class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        
        def order(prefix, suffix):
            if len(suffix) == 1:
                return [prefix+suffix]
            results = []
            for i in range(len(suffix)):
                results.extend(order(prefix+[suffix[i]], suffix[:i]+suffix[i+1:]))
            return results
        
        return order([], nums)