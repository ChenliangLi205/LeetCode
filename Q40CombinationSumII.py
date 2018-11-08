import time

T1 = ([10,1,2,7,6,1,5], 8)


def findSuffix(s, p):
    suffixLen = len(s)
    while suffixLen > 0:
        if s[len(s)-suffixLen:] == p[:suffixLen]:
            break
        suffixLen -= 1
    return suffixLen


def solution(candidates, target):
    def calculate(nums, tar):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            if tar == nums[0]:
                return [[nums[0]]]
            else:
                return []
        if tar < nums[0]:
            return []
        cnt = 1
        while cnt < len(nums):
            if nums[cnt] != nums[0]:
                break
            cnt += 1
        results = []
        prefix = []
        for i in range(cnt + 1):
            if sum(prefix) == tar:
                results.append(prefix)
                break
            if sum(prefix) > tar:
                break
            subResults = calculate(nums[cnt:], tar - i * nums[0])
            if len(subResults):
                for s in subResults:
                    results.append(prefix + s)
            prefix.append(nums[0])

        return results

    candidates.sort()
    return calculate(candidates, target)


if __name__ == '__main__':
    t1 = time.time()
    head = solution(*T1)
    print(head)
    print(time.time()-t1)
