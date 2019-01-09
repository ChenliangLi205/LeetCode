class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        left, right = 0,3
        results = 0
        while right <= len(A):
            sli = A[left:right]
            if sli[1] - sli[0] == sli[2] - sli[1]:
                c = sli[1] - sli[0]
                new = right
                while new < len(A):
                    if A[new] - sli[-1] == c:
                        sli.append(A[new])
                        new += 1
                    else:
                        new -= 1
                        break
                results += sum(range(1, len(sli)-1))
                left = new
                right = left+3
            else:
                left += 1
                right += 1
        return results