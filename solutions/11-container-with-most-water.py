class Solution:
    def maxArea(self, heights):
        max_area = 0
        max_width = len(heights) - 1
        left, right = 0, max_width

        for width in range(max_width, 0, -1):
            max_area = max(min(heights[left], heights[right]) * width, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area