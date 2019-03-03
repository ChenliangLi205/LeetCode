class Bucket(object):
    def __init__(self):
        self.empty=True
        self.minVal=0
        self.maxVal=0
    
    def put(self, val):
        if self.empty:
            self.minVal = val
            self.maxVal = val
            self.empty = False
        else:
            if val < self.minVal:
                self.minVal = val
            if val > self.maxVal:
                self.maxVal = val
        return

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return abs(nums[1]-nums[0])
        minNum = float(min(nums))
        maxNum = float(max(nums))
        if minNum == maxNum:
            return 0
        bucketSize = (maxNum - minNum) / float(len(nums))
        start = minNum
        buckets = []
        while start <= maxNum:
            buckets.append(Bucket())
            start += bucketSize
        buckets.append(Bucket())
        for n in nums:
            buckets[int((n-minNum)/bucketSize)].put(n)
        lastIdx = 0
        currIdx = 1
        maxGap = 0
        while currIdx < len(buckets):
            if buckets[currIdx].empty:
                currIdx += 1
            else:
                maxGap = max(maxGap, buckets[currIdx].minVal - buckets[lastIdx].maxVal)
                lastIdx = currIdx
                currIdx += 1
        return maxGap
        