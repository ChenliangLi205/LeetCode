import time

T1 = ("babba", "bbb")
T2 = ("mississippi", "issip")


def findSuffix(s, p):
    suffixLen = len(s)
    while suffixLen > 0:
        if s[len(s)-suffixLen:] == p[:suffixLen]:
            break
        suffixLen -= 1
    return suffixLen


def solution(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    stateDict, needleSet, needleLen = dict(), set(needle), len(needle)
    state = 0
    pb = needle[:state]
    while state < needleLen:
        for char in needleSet:
            s = pb+char
            stateDict[state, char] = findSuffix(s, needle)
        state += 1
        pb = needle[:state]
    state = 0
    for i in range(len(haystack)):
        char = haystack[i]
        if char not in needleSet:
            state = 0
            continue
        state = stateDict[state, char]
        if state == needleLen:
            return i-needleLen+1
    return -1


if __name__ == '__main__':
    t1 = time.time()
    head = solution(*T1)
    print(head)
    print(time.time()-t1)
