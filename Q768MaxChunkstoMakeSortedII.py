class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 0:
            return 0
        dp = [1]*len(arr)
        Max = [0]*len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[Max[i-1]]:
                Max[i] = i
            else:
                Max[i] = Max[i-1]
        for i in range(1, len(arr)):
            j = i-1
            while j>=0:
                if min(arr[j+1:i+1]) >= arr[Max[j]]:
                    break
                else:
                    j = Max[j]-1
            if j < 0:
                dp[i] = 1
            else:
                dp[i] = dp[j]+1
        return dp[-1]