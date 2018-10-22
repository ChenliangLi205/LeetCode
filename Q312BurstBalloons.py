S = [35,16,83,87,84,59,48,41,20,54]
S1 = [2,3,7,9,1,8,2]
S2 = [7, 6, 5, 4, 3, 2, 8]


def solution(nums):
    nums = [1] + nums + [1]
    length = len(nums)
    dp = [[0]*length for _ in range(length)]

    def calculate(i, j):
        if dp[i][j]:
            return dp[i][j]
        if j == i+1:
            return 0
        else:
            max_coins = 0
            for k in range(i+1, j):
                max_coins = max(max_coins, calculate(i, k)+calculate(k, j)+nums[i]*nums[k]*nums[j])
            dp[i][j] = max_coins
            return max_coins

    return calculate(0, length-1)


if __name__ == '__main__':
    print(solution(S2))