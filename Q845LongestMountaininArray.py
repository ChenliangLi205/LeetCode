class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        start, end = 0, 1
        up = True
        maxLen = 0
        while end < len(A):
            if up:
                if A[end] > A[end - 1]:
                    end += 1
                elif A[end] < A[end - 1]:
                    if start == end - 1:  # no up
                        start = end
                        end += 1
                    else:
                        maxLen = max(maxLen, end - start + 1)
                        up = False
                        end += 1
                else:
                    start = end
                    end += 1

            else:
                if A[end] < A[end - 1]:
                    maxLen = max(maxLen, end - start + 1)
                    end += 1
                elif A[end] > A[end - 1]:
                    up = True
                    start = end - 1
                else:
                    up = True
                    start = end
                    end += 1
        return maxLen
