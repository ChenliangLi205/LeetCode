class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [n[0] for n in matrix]
        results = []
        cnt, row, col, loc = 0, len(matrix), len(matrix[0]), 0
        while True:
            left, right = loc, col - 1 - loc
            up, down = loc, row - 1 - loc
            if left > right or up > down:
                break
            for j in range(left, right + 1):
                results.append(matrix[up][j])
            if up == down:
                break
            for i in range(up + 1, down + 1):
                results.append(matrix[i][right])
            if left == right:
                break
            for j in range(right - 1, left - 1, -1):
                results.append(matrix[down][j])
            for i in range(down - 1, up, -1):
                results.append(matrix[i][left])
            loc += 1
        return results
