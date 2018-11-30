class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [n[0] for n in matrix]
        rows, cols = len(matrix), len(matrix[0])
        up, r, c = True, 0, 0
        result = []
        while True:
            if up:
                result.append(matrix[r][c])
                if r == rows - 1 and c == cols - 1:
                    break
                if r == 0:
                    if c != cols - 1:
                        c += 1
                        up = False
                        continue
                    else:
                        r += 1
                        up = False
                        continue
                if c == cols - 1:
                    r += 1
                    up = False
                    continue
                r -= 1
                c += 1
            else:
                result.append(matrix[r][c])
                if r == rows - 1 and c == cols - 1:
                    break
                if r == rows - 1:
                    c += 1
                    up = True
                    continue
                if c == 0:
                    if r != rows - 1:
                        r += 1
                        up = True
                        continue
                    else:
                        c += 1
                        up = True
                        continue
                r += 1
                c -= 1
        return result

