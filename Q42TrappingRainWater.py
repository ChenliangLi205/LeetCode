class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        result = 0
        leftMax, rightMax = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        for i in range(1, len(height) - 1):
            result += min(leftMax[i], rightMax[i]) - height[i]
        return result
