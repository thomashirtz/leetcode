class Solution:
    def trap(self, height):
        length = len(height)
        if not height or length < 3:
            return 0

        left_max = [0] * length
        right_max = [0] * length

        for i in range(length - 1):
            left_max[i+1] = max(left_max[i], height[i])

        for i in reversed(range(1, length)):
            right_max[i-1] = max(right_max[i], height[i])

        volume = [max(min(left_max[i], right_max[i]) - height[i], 0) for i in range(length)]
        return sum(volume)