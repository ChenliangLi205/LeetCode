import time

T1 = ("adceb", "*a*b")
T2 = ("acdcb", "a*c?b")
T3 = ("aab", "c*a*b")


def solution(s, p):
    lenS, lenP = len(s), len(p)
    if lenS == lenP == 0:
        return True
    state, fsm = 0, dict()
    for char in s:
        fsm[(state, char)] = state + 1
        state += 1
    target = state
    stateSet = set()
    stateSet.add(0)
    for char in p:
        if len(stateSet) == 0:
            return False
        if char == "?":
            stateSet = {x + 1 for x in stateSet}
        elif char == "*":
            min_ = min(stateSet)
            stateSet = {x for x in range(min_, target + 1)}
        else:
            newStates = set()
            for x in stateSet:
                if (x, char) in fsm:
                    newStates.add(x+1)
            stateSet = newStates
    return target in stateSet


if __name__ == '__main__':
    t1 = time.time()
    head = solution(*T3)
    print(head)
    print(time.time()-t1)
