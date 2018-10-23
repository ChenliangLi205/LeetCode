import time

T1 = ([2, 5, 7], 10000)
T2 = ([1, 2, 5], 11)
T3 = ([1], 0)
T4 = ([2], 1)


def solution(coins, amount):
    if amount == 0:
        return 0
    if len(coins) == 0:
        if amount == 0:
            return 0
        else:
            return -1
    coins.sort(reverse=True)
    if coins[-1] > amount:
        return 0
    to_ddelete = 0
    for i in range(len(coins)):
        if coins[i] > amount:
            to_ddelete = i

    dp = [0] * (amount + 1)
    for c in coins:
        dp[c] = 1
    for i in range(len(dp)):
        if not dp[i]:
            access = []
            for c in coins:
                j = i - c
                if j > 0:
                    if dp[j]:
                        access.append(dp[j] + 1)
            if len(access) != 0:
                dp[i] = min(access)
    if dp[-1]:
        return dp[-1]
    else:
        return -1


if __name__ == '__main__':
    t1 = time.time()
    print(solution(*T4))
    print(time.time() - t1)
