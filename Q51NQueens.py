import time
from copy import deepcopy

T1 = 4


def solution(n):
    if n == 1:
        return ["Q"]
    if n < 4:
        return []
    board, vboard = [["."]*n for _ in range(n)], [[0]*n for _ in range(n)]
    results = list()

    def BackTrack(k):
        if k >= n:
            return
        for i in range(n):
            if not vboard[k][i]:
                SetBoard(k, i)
                if k == n-1:
                    resultBoard = []
                    for row in board:
                        resultBoard.append(''.join(row))
                    results.append(resultBoard)
                BackTrack(k+1)
                UnSetBoard(k, i)

    def SetBoard(row, col):
        board[row][col] = "Q"
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
        board[row][col] = "."
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
    return results


def ShowBoard(board):
    for row in board:
        print(row)

if __name__ == '__main__':
    t1 = time.time()
    head = solution(T1)
    for board in head:
        ShowBoard(board)
        print('\n')
    print(time.time()-t1)
