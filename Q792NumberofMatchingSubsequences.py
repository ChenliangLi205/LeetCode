import time

T1 = ("abcbcdef", ["acc", "cbb"])
T2 = ("a", ["a", "b", "cbb"])


def solution(S, words):
    char2locs = dict()
    for i in range(len(S)):
        char = S[i]
        if char not in char2locs:
            char2locs[char] = [i]
        else:
            char2locs[char].append(i)
    matchCnt = 0
    for w in words:
        currentLoc = -1
        for i in range(len(w)):
            char = w[i]
            find = False
            for j in char2locs.setdefault(char, []):
                if j > currentLoc:
                    currentLoc = j
                    find = True
                    break
            if not find:
                break
            if i == len(w) - 1:
                matchCnt += 1
    return matchCnt


if __name__ == '__main__':
    t1 = time.time()
    print(solution(*T2))
    print(time.time()-t1)
