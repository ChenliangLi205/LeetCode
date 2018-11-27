class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        if cols == 0:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        colNs = [matrix[i][-1] for i in range(rows)]
        left, right = 0, rows
        while left < right:
            mid = (left + right) // 2
            if target == colNs[mid]:
                return True
            elif target > colNs[mid]:
                left = mid + 1
            else:
                right = mid
        r = right
        rowNs = matrix[r]
        left, right = 0, cols
        while left < right:
            mid = (left + right) // 2
            if target == rowNs[mid]:
                return True
            elif target > rowNs[mid]:
                left = mid + 1
            else:
                right = mid
        return False
