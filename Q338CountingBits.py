class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0, 1, 1, 2, 1, 2, 2, 3]
        new_to_extend = [1, 2, 2, 3, 2, 3, 3, 4]
        now = 8

        while num // now > 1:
            now *= 2
            bits.extend(new_to_extend)
            new_to_extend.extend([n + 1 for n in new_to_extend])

        if num // now == 0:
            return bits[: num + 1]

        if num // now == 1:
            bits.extend([new_to_extend[i] for i in range(num % now + 1)])
            return bits