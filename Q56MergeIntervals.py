# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        newIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = newIntervals[-1]
            if cur.start > last.end:
                newIntervals.append(cur)
            else:
                last.end = max(cur.end, last.end)
        return newIntervals
