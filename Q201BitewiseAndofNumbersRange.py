class Solution:
    def rangeBitwiseAnd(self, m: 'int', n: 'int') -> 'int':
        result = 0
        rate = 1
        while n>0:
            if n==m:
                result += rate*(n%2)
            rate *= 2
            n //= 2
            m //= 2
        return result