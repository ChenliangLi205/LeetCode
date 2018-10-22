import time

a = [2, 3, -2, 4]


def solution(nums):
    if len(nums) == 1:
        return nums[0]
    max_ = 0
    so_far = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            so_far = 1
            continue
        so_far *= nums[i]
        max_ = max(max_, so_far)
    so_far = 1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 0:
            so_far = 1
            continue
        so_far *= nums[i]
        max_ = max(max_, so_far)
    return max_


if __name__ == '__main__':
    t1 = time.time()
    print(solution(a))
    print(time.time()-t1)
