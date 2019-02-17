class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        cnt = 1
        for i in range(2, n):
            cnt *= i
        result = ""
        nums = [_ for _ in range(1, n+1)]
        k-=1
        while len(result) < n-1:
            idx = int(k/cnt)
            result += str(nums[idx])
            nums.pop(idx)
            k %= cnt
            cnt //= len(nums)
        return result+str(nums[0])