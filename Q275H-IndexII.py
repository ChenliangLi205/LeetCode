class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        if citations[0] >= len(citations):
            return len(citations)
        hidx = 0
        for l in range(1, len(citations)):
            if citations[-1-l] <= l and citations[-l] >= l:
                hidx = max(l, hidx)
            if citations[-l] < l:
                break
        return hidx