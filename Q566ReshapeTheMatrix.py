class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        cols = len(nums[0])

        if rows * cols != r * c:
            return nums

        newNums = [[0] * c for _ in range(r)]
        x, y = 0, 0
        for i in range(rows):
            for j in range(cols):
                newNums[x][y] = nums[i][j]
                y += 1
                if y == c:
                    x += 1
                    y = 0
        return newNums
