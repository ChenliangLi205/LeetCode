class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        citations.sort(reverse=True)
        if citations[-1] >= len(citations):
            return len(citations)
        hidx = 0
        for i in range(1, len(citations)):
            if citations[i] <= i and citations[i-1] >= i:
                hidx = max(hidx, i)
            if citations[i] < i:
                break
        return hidx