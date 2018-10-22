import time
B1 = "WWRRBBWW"
H1 = "WRBRW"
B2 = "RBYYBBRRB"
H2 = "YRBGB"
B3 = "R"
H3 = "RR"


def remove_balls(b):
    while len(b) >= 3:
        modified = False
        for i in range(2, len(b)):
            if b[i] == b[i - 1] == b[i - 2]:
                modified = True
                j = i+1
                while j < len(b) and b[j] == b[i]:
                    j += 1
                b = b[:i - 2] + b[j:]
                break
        if not modified:
            break
    return b


def solution(board, hand):
    q = [(board, hand, 0)]
    min_in = 99
    while len(q):
        b, h, in_ = q.pop()
        b = remove_balls(b)
        if in_ > min_in:
            continue
        if len(b) == 0:
            min_in = min(min_in, in_)
        elif len(h) == 0:
            continue
        if len(b) == 1:
            cnt = 0
            for j in range(len(h)):
                if h[j] == b[0]:
                    cnt += 1
            if cnt >= 2:
                min_in = min(min_in, in_+2)
            continue
        for i in range(1, len(b)):
            if b[i] == b[i-1] and b[i] in h:
                new_b = b[:i-1] + b[i+1:]
                for j in range(len(h)):
                    if h[j] == b[i]:
                        new_h = h[:j] + h[j+1:]
                        break
                q.append((new_b, new_h, in_+1))
            if b[i] != b[i-1] and b[i] in h:
                if i == len(b)-1:
                    new_b = b+b[i]
                    for j in range(len(h)):
                        if h[j] == b[i]:
                            new_h = h[:j] + h[j+1:]
                            break
                    q.append((new_b, new_h, in_ + 1))
                elif b[i+1] != b[i]:
                    new_b = b[:i+1]+b[i:]
                    for j in range(len(h)):
                        if h[j] == b[i]:
                            new_h = h[:j] + h[j+1:]
                            break
                    q.append((new_b, new_h, in_+1))
    if min_in == 99:
        return -1
    else:
        return min_in


if __name__ == '__main__':
    t1 = time.time()
    print(solution(B3, H3))
    print(time.time()-t1)