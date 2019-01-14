class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if len(T) == 0:
            return [0]
        results = [0] * len(T)
        for i in range(len(T)-2, -1, -1):
            if T[i+1] > T[i]:
                results[i] = 1
            else:
                higher = False
                j = i + 1 + results[i+1]
                while j < len(T):
                    if T[i] < T[j]:
                        higher = True
                        break
                    if results[j] == 0:
                        break
                    j += results[j]
                if higher:
                    results[i] = j-i
                else:
                    results[i] = 0
        return results