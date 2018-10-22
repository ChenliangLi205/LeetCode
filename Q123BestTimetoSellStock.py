import time
# Time Limit Exceeded
# To be modified
P1 = [3,3,5,0,0,3,1,4]
P2 = [1,2,3,4,5]
P3 = [7,6,4,3,1]
P4 = [3,3,5,0,0,8,1,4,9,0,9]
P5 = [2,1,4]
P6 = [1,4,2,9,4,3]
P7 = [1,2,3,4,5]
P8 = [2,1,2,0,1]


def solution(prices):
    k = 2
    dp = [[0] * len(prices) for _ in range(k+1)]
    for k in range(1, len(dp)):
        for i in range(len(prices)):
            max_ = dp[k][i-1]
            if k-1 == 0:
                for j in range(i):
                    max_ = max(max_, prices[i]-prices[j])
            else:
                for j in range(2*k-3, i-1):
                    max_ = max(max_, dp[k-1][j]+prices[i]-prices[j+1])
            dp[k][i] = max_
    return max([dp[k_][len(prices)-1] for k_ in range(k+1)])


if __name__ == '__main__':
    t1 = time.time()
    print(solution(P8))
    print(time.time()-t1)
