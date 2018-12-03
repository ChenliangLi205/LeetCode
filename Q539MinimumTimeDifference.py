class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def timeMinus(t1, t2):
            h1, m1 = t1.split(":")
            h2, m2 = t2.split(":")
            h1, h2, m1, m2 = int(h1), int(h2), int(m1), int(m2)
            if h1 < h2 or (h1 == h2 and m1 < m2):
                h1 += 24
            return (h1 - h2) * 60 + m1 - m2

        timePoints.sort()
        min_ = timeMinus(timePoints[0], timePoints[-1])
        for i in range(1, len(timePoints)):
            min_ = min(min_, timeMinus(timePoints[i], timePoints[i - 1]))
        return min_