import time

T1 = ("babgbag", "bag")
T2 = ("rabbbit", "rabbit")


def solution(s, t):
    if len(t) == 0:
        return 1
    if len(s) == 0:
        return 0
    fsm = dict()
    state = 0
    for char in t:
        fsm[state, char] = state+1
        state += 1
    target = state
    currentStates = dict()
    currentStates[0] = 1
    for char in s:
        addings = dict()
        for state in currentStates:
            newState = fsm.setdefault((state, char), 0)
            if newState == 0:
                continue
            elif newState not in addings:
                addings[newState] = currentStates[state]
            else:
                addings[newState] += currentStates[state]
        for state in addings:
            if state not in currentStates:
                currentStates[state] = 0
            currentStates[state] += addings[state]
    return currentStates.setdefault(target, 0)


if __name__ == '__main__':
    t1 = time.time()
    head = solution(*T1)
    print(head)
    print(time.time()-t1)
