class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[], ["()"], ["(())", "()()"]]
        if n <= 2:
            return dp[n]
        for i in range(3, n+1):
            newResultSet = set()
            newResultSet.add("("*i+")"*i)
            for pattern in dp[-1]:
                newResultSet.add("("+pattern+")")
            for j in range(1, i):
                left, right = j, i-j
                for patternLeft in dp[left]:
                    for patternRight in dp[right]:
                        newResultSet.add(patternLeft+patternRight)
            dp.append(list(newResultSet))
        return dp[-1]