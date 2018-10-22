import time
# TIME LIMIT EXCEEDED
# TO BE MODIFIED
S = "acdcb"
P = "a*c?b"
S1 = "cdb"
P1 = "c?b"
S2 = "aa"
P2 = "a"
S3 = "ho"
P3 = "ho**"
S4 = "aa"
P4 = "*"
S5 = "aab"
P5 = "c*a*b"
S6 = "ba"
P6 = "*a*"
S7 = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
P7 = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"


def solution(s, p):
    def matches(arr_s, arr_p):
        if len(arr_s) == 0:
            if len(arr_p) == 0 or arr_p == "*":
                return True
            else:
                return False
        elif len(arr_p) == 0:
            return False
        match = True
        for i in range(len(arr_p)):
            if arr_p[i] == '*':
                if i == len(arr_p)-1:
                    match = True
                    break
                p_unmatched = arr_p[i+1:]
                sub_match = False
                for k in range(len(arr_s)-1, i-1, -1):
                    if matches(arr_s[k:], p_unmatched):
                        sub_match = True
                        break
                if sub_match:
                    match = True
                    break
                else:
                    match = False
                    break
            elif i > len(arr_s)-1:
                match = False
                break
            elif i == len(arr_p)-1 and i < len(arr_s)-1:
                match = False
                break
            elif arr_p[i] != '?' and arr_p[i] != arr_s[i]:
                match = False
                break
        return match
    if len(p) > 1:
        to_keep = [i for i in range(len(p)) if i==0 or p[i]!='*' or p[i-1]!='*']
        p = ''.join([p[i] for i in to_keep])
    return matches(s, p)


if __name__ == '__main__':
    t1 = time.time()
    print(solution(S7, P7))
    print(time.time()-t1)
