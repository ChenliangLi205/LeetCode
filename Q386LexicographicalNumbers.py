class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        results = [n for n in range(1, n+1)]
        results.sort(key= lambda x: str(x))
        return results