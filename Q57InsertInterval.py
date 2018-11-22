# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        newIntervals = []
        for i in range(len(intervals)):
            cur = intervals[i]
            if cur.start < newInterval.start:
                newIntervals.append(cur)
                continue
            if i == 0:
                newIntervals.append(cur)
                continue
            last = newIntervals[-1]
            if last.end > cur.end:
                continue
            elif cur.start > last.end:
                newIntervals.append(cur)
            else:
                last.end = cur.end
        return newIntervals