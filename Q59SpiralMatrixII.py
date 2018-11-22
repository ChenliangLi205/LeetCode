class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        matrix = [[0]*n for _ in range(n)]
        layer, num = 0, 1
        while n-layer*2 > 0:
            rol, col, length = layer, layer, n-layer*2
            for i in range(length):
                matrix[rol][col+i] = num
                num += 1
            col += length-1
            for i in range(length):
                if not matrix[rol+i][col]:
                    matrix[rol+i][col] = num
                    num += 1
            rol += length-1
            for i in range(length):
                if not matrix[rol][col-i]:
                    matrix[rol][col-i] = num
                    num += 1
            col -= length-1
            for i in range(length):
                if not matrix[rol-i][col]:
                    matrix[rol-i][col] = num
                    num += 1
            layer += 1
        return matrix