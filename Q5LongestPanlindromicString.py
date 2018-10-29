import time

T1 = "abcdefijkabcdefe"


def solution(s):
    if len(s) == 1:
        return s

    char2loc = dict()
    for i in range(len(s)):
        if s[i] not in char2loc:
            char2loc[s[i]] = [i]
        else:
            char2loc[s[i]].append(i)
    if len(char2loc) == 1:
        return s

    longest = ''

    for i in range(len(s)):
        appearances = char2loc[s[i]]
        if len(appearances) < 2:
            if len(longest) == 0:
                longest = s[i]
        else:
            for j in range(len(appearances) - 1, -1, -1):
                i_, j_ = i, appearances[j]
                if len(longest) >= j_ - i_ + 1:
                    continue
                if j_ - i_ <= 2:
                    longest = s[i_:j_ + 1]
                is_pan = True
                i_, j_ = i_ + 1, j_ - 1
                while j_ > i_:
                    if s[j_] != s[i_]:
                        is_pan = False
                        break
                    i_, j_ = i_ + 1, j_ - 1
                i_, j_ = i, appearances[j]
                if is_pan:
                    longest = s[i_:j_ + 1]
    return longest


if __name__ == '__main__':
    t1 = time.time()
    print(solution(T1))
    print(time.time() - t1)
