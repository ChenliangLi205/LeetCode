import time

T1 = "abcdddab"


def solution(s):
    if len(s) == 1:
        return 1
    visited = dict()
    i, j = 0, 0
    length, max_len = 0, 0
    while j < len(s):
        if s[j] not in visited:
            visited[s[j]] = j
            length += 1
            j += 1
            max_len = max(max_len, length)
        else:
            i_new = visited[s[j]] + 1
            for k in range(i, i_new):
                del visited[s[k]]
            i = i_new
            visited[s[j]] = j
            length = j - i + 1
            j += 1
            max_len = max(max_len, length)
    return max_len


if __name__ == '__main__':
    t1 = time.time()
    print(solution(T1))
    print(time.time()-t1)
