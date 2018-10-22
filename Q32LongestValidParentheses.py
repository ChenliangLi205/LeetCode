import time

S = ")()())"
S1 = "()(()"
S2 = "(()()()"
S3 = "()()"


def solution(s):
    if len(s) <= 1:
        return 0
    left = 0
    right = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] == ')':
            right += 1
        else:
            left += 1
        if left == right:
            max_length = max(left*2, max_length)
        if right > left:
            left = right = 0
    left = right = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_length = max(left*2, max_length)
        if left > right:
            left = right = 0
    return max_length

if __name__ == '__main__':
    t1 = time.time()
    print(solution(S))
    print(time.time()-t1)
    # new_b = [[0] * 9 for _ in range(9)]
    # for i in range(len(board2)):
    #     for j in range(len(board2[i])):
    #         if board2[i][j] != ".":
    #             new_b[i][j] = int(board2[i][j])
    # print(find_num(new_b, 0, 0))
