class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def calculate(nums, tar):
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                if tar % nums[0] == 0:
                    return [list(nums[0] for _ in range(tar // nums[0]))]
                else:
                    return []
            if tar < nums[0]:
                return []
            if tar == nums[0]:
                return [[nums[0]]]
            results = []
            prefix = []
            for j in range(tar // nums[0] + 1):
                if sum(prefix) == tar:
                    results.append(prefix)
                    break
                subResults = calculate(nums[1:], tar - j * nums[0])
                if len(subResults):
                    for s in subResults:
                        results.append(prefix + s)
                prefix.append(nums[0])
            return results

        candidates.sort()
        return calculate(candidates, target)