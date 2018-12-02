import time

T1 = [[1,0,1,0],[1,1,1,1],[1,1,1,1],[1,0,0,1]]


def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row == col == 1:
        return matrix
    dp = [[-1] * (col + 2) for _ in range(row + 2)]
    unassigned = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                dp[i + 1][j + 1] = 0
            else:
                unassigned.append((i + 1, j + 1))
    target = 0
    while len(unassigned):
        remain_unassigned = []
        for i, j in unassigned:
            candidates = [dp[i + 1][j], dp[i - 1][j], dp[i][j + 1], dp[i][j - 1]]
            if target in candidates:
                dp[i][j] = target + 1
            else:
                remain_unassigned.append((i, j))
        unassigned = remain_unassigned
        target += 1

    for i in range(row):
        for j in range(col):
            matrix[i][j] = dp[i + 1][j + 1]
    return matrix


if __name__ == '__main__':
    t1 = time.time()
    m = solution(T1)
    for i in range(len(m)):
        print(m[i])
    print(time.time()-t1)
