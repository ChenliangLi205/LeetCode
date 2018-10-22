import time

G =[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
G1 = [[1,2],[5,6],[1,1]]
G2 = [[1]]


def solution(grid):
    if len(grid) == 0:
        return 0
    dp = [[0]*len(grid[0]) for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for j in range(1, len(grid[0])):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, len(grid)):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, len(grid)):
        if i >= len(grid[i]):
            break
        dp[i][i] = min(dp[i-1][i], dp[i][i-1]) + grid[i][i]
        for j in range(i+1, len(grid[i])):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        for k in range(i+1, len(grid)):
            dp[k][i] = min(dp[k-1][i], dp[k][i-1]) + grid[k][i]
    return dp[-1][-1]


if __name__ == '__main__':
    t1 = time.time()
    print(solution(G2))
    print(time.time()-t1)
