class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) <= 1:
            return asteroids
        stack = [asteroids[0]]
        for size in asteroids[1:]:
            if len(stack) == 0:
                stack.append(size)
                continue
            if size * stack[-1] > 0:
                stack.append(size)
            elif size > 0 and stack[-1] < 0:
                stack.append(size)
            else:
                boom = False
                while len(stack) and stack[-1]>0:
                    size_ = stack.pop(-1)
                    if size_ > abs(size):
                        stack.append(size_)
                        boom = True
                        break
                    if size_ == abs(size):
                        boom = True
                        break
                if not boom:
                    stack.append(size)
        return stack