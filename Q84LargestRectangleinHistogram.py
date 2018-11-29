class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)
        if length == 0:
            return 0
        if length == 1:
            return heights[0]
        if length == 2:
            return max(min(heights) * 2, max(heights))
        # left[i] stores the number of consecutive diagrams that are heigher than heights[i] in heights[:i]
        # right[i] stores the number of consecutive diagrams that are higher than heights[i] in heights[1+1:]
        left, right = [0] * length, [0] * length
        for i in range(1, length):
            j = i - 1
            while j >= 0:
                if heights[j] < heights[i]:
                    left[i] = i - j - 1
                    break
                else:
                    left[i] += left[j] + 1
                    j = j - left[j] - 1
        for i in range(length - 2, -1, -1):
            j = i + 1
            while j < length:
                if heights[j] < heights[i]:
                    right[i] = j - i - 1
                    break
                else:
                    right[i] += right[j] + 1
                    j = j + right[j] + 1
        result = 0
        for i in range(length):
            result = max(result, (left[i] + right[i] + 1) * heights[i])
        return result
