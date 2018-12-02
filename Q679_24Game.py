S = [4, 1, 8, 7]
S1 = [3,3,7,7]
S2 = [1, 2, 1, 2]


def satisfy(ns, target):

    if len(ns) == 2:
        if ns[0] * ns[1] == target:
            return True
        if ns[0] + ns[1] == target:
            return True
        if ns[0] - ns[1] == target or ns[1] - ns[0] == target:
            return True
        if ns[0] != 0:
            if target-1e-4 <= ns[1] / ns[0] <= target+1e-4:
                return True
        if ns[1] != 0:
            if target-1e-4 <= ns[0] / ns[1] <= target+1e-4:
                return True
        return False

    if len(ns) == 3:
        for i in range(3):
            remain = [ns[j] for j in range(3) if j != i]
            if satisfy(remain, target-ns[i]):
                return True
            if satisfy(remain, target+ns[i]) or satisfy(remain, ns[i]-target):
                return True
            if ns[i] != 0:
                if satisfy(remain, target/ns[i]):
                    return True
                if target != 0:
                    if satisfy(remain, ns[i]/target):
                        return True
                if satisfy(remain, ns[i] * target):
                    return True
        return False

    if len(ns) == 4:
        for i in range(4):
            remain = [ns[j] for j in range(4) if j != i]
            if satisfy(remain, target-ns[i]):
                return True
            if satisfy(remain, target+ns[i]):
                return True
            if satisfy(remain, ns[i]-target):
                return True
            if ns[i] != 0:
                if satisfy(remain, target/ns[i]):
                    return True
                if target != 0:
                    if satisfy(remain, ns[i]/target):
                        return True
                if satisfy(remain, ns[i] * target):
                    return True

        for i in range(4):
            for j in range(i+1, 4):
                remain = [ns[k] for k in range(4) if k != j and k != i]
                comb = [ns[i]+ns[j], ns[i]-ns[j], ns[j]-ns[i], ns[i]*ns[j]]
                if ns[i] != 0:
                    comb.append(ns[j]/ns[i])
                if ns[j] != 0:
                    comb.append(ns[j]/ns[i])
                for c in comb:
                    if satisfy(remain, target-c):
                        return True
                    if satisfy(remain, target+c):
                        return True
                    if satisfy(remain, c-target):
                        return True
                    if c != 0:
                        if satisfy(remain, target/c):
                            return True
                        if target != 0:
                            if satisfy(remain, c/target):
                                return True
                        if satisfy(remain, c*target):
                            return True
        return False


def solution(nums):
    return satisfy(nums, 24.)


if __name__ == '__main__':
    print(solution(S2))
