# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import bisect


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.starts = []
        self.ends = []
        self.intervals = []
        self.numSet = set()
        return

    def insertInterval(self, val, pos):
        self.intervals.insert(pos, Interval(val, val))
        self.starts.insert(pos, val)
        self.ends.insert(pos, val)
        return

    def mergeInterval(self, pos):
        self.intervals[pos].end = self.intervals[pos + 1].end
        self.ends[pos] = self.ends[pos + 1]
        self.starts.pop(pos + 1)
        self.ends.pop(pos + 1)
        self.intervals.pop(pos + 1)
        return

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.numSet:
            return
        else:
            self.numSet.add(val)

        if len(self.intervals) == 0:
            self.insertInterval(val, 0)
            return

        endPos = bisect.bisect_left(self.ends, val)

        if endPos >= len(self.ends):
            if val == self.ends[-1] + 1:
                self.intervals[-1].end += 1
                self.ends[-1] += 1
            else:
                self.insertInterval(val, len(self.intervals))
            return

        startPos = bisect.bisect_left(self.starts, val)

        if startPos == 0:
            if val == self.starts[0] - 1:
                self.intervals[0].start -= 1
                self.starts[0] -= 1
            else:
                self.insertInterval(val, 0)
            return

        if startPos == endPos:
            if self.ends[endPos - 1] == val - 1:
                if self.starts[startPos] == val + 1:
                    self.mergeInterval(endPos - 1)
                else:
                    self.intervals[endPos - 1].end += 1
                    self.ends[endPos - 1] += 1
                return
            elif self.starts[startPos] == val + 1:
                self.intervals[startPos].start -= 1
                self.starts[startPos] -= 1
                return
            else:
                self.insertInterval(val, startPos)
                return
        return

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals



        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(val)
        # param_2 = obj.getIntervals()