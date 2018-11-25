class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n < 4:
            return 0
        vboard = [[0]*n for _ in range(n)]
        results = [0]

        def BackTrack(k):
            if k >= n:
                return
            for i in range(n):
                if not vboard[k][i]:
                    SetBoard(k, i)
                    if k == n-1:
                        results[0] += 1
                    BackTrack(k+1)
                    UnSetBoard(k, i)

        def SetBoard(row, col):
            manipulated = set()
            for i in range(n):
                vboard[row][i] += 1
                manipulated.add((row, i))
            for i in range(n):
                if (i, col) not in manipulated:
                    vboard[i][col] += 1
                    manipulated.add((i, col))
            startRow, startCol = row, col
            while startRow > 0 and startCol > 0:
                startRow -= 1
                startCol -= 1
            while startRow < n and startCol < n:
                if (startRow, startCol) not in manipulated:
                    vboard[startRow][startCol] += 1
                    manipulated.add((startRow, startCol))
                startRow += 1
                startCol += 1
            startRow, startCol = row, col
            while startRow > 0 and startCol < n-1:
                startRow -= 1
                startCol += 1
            while startRow < n and startCol >= 0:
                if (startRow, startCol) not in manipulated:
                    vboard[startRow][startCol] += 1
                startRow += 1
                startCol -= 1

        def UnSetBoard(row, col):
            manipulated = set()
            for i in range(n):
                vboard[row][i] -= 1
                manipulated.add((row, i))
            for i in range(n):
                if (i, col) not in manipulated:
                    vboard[i][col] -= 1
                    manipulated.add((i, col))
            startRow, startCol = row, col
            while startRow > 0 and startCol > 0:
                startRow -= 1
                startCol -= 1
            while startRow < n and startCol < n:
                if (startRow, startCol) not in manipulated:
                    vboard[startRow][startCol] -= 1
                    manipulated.add((startRow, startCol))
                startRow += 1
                startCol += 1
            startRow, startCol = row, col
            while startRow > 0 and startCol < n-1:
                startRow -= 1
                startCol += 1
            while startRow < n and startCol >= 0:
                if (startRow, startCol) not in manipulated:
                    vboard[startRow][startCol] -= 1
                startRow += 1
                startCol -= 1

        BackTrack(0)
        return results[0]