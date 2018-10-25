class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        target = 0
        solutions = []
        nums.sort()
        num2cnt = {}
        nums_nodup = []
        for n in nums:
            if n not in num2cnt.keys():
                num2cnt[n] = 1
                nums_nodup.append(n)
            else:
                num2cnt[n] += 1

        for i in range(len(nums_nodup)):
            first_num = nums_nodup[i]

            if num2cnt[first_num] >= 3:
                if first_num * 3 == target:
                    solutions.append([first_num, first_num, first_num])

            if num2cnt[first_num] >= 2:
                last_num = target - 2 * first_num
                if last_num > first_num and last_num in num2cnt:
                    solutions.append([first_num, first_num, last_num])

            for j in range(i + 1, len(nums_nodup)):
                mid_num = nums_nodup[j]
                last_num = target - first_num - mid_num
                if last_num < mid_num:
                    break
                if last_num > mid_num and last_num in num2cnt:
                    solutions.append([first_num, mid_num, last_num])
                if last_num == mid_num:
                    if last_num in num2cnt and num2cnt[last_num] >= 2:
                        solutions.append([first_num, mid_num, last_num])
        return solutions

