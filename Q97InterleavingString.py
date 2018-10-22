import time

T1 = ("aabcc", "dbbca", "aadbbcbcac")
T2 = ("aabcc", "dbbca", "aadbbbaccc")
T3 = ("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
T4 = ("aabbcc", "", "aabbcc")
T5 = ("db", "b", "cbb")


def solution(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    if len(s1) == 0:
        return s3 == s2
    if len(s2) == 0:
        return s3 == s1
    dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0] = True
    for j in range(1, len(s2)+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    for i in range(1, len(s1)+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    for i in range(1, len(s1)+1):
        for j in range(i, len(s2)+1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        for j in range(i, len(s1)+1):
            if i > len(s2):
                break
            dp[j][i] = (dp[j-1][i] and s1[j-1] == s3[i+j-1]) or (dp[j][i-1] and s2[i-1] == s3[i+j-1])
    return dp[-1][-1]


if __name__ == '__main__':
    t1 = time.time()
    print(solution(*T5))
    # print(solution(*T2))
    print(time.time()-t1)
