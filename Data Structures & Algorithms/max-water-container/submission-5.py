#need to return single value
#stored water = min(height 1, height 2) * base (right - left)
#need 2 pointers start at bounds work in, since bounded by lower heigh, move lower hight pointer


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxWater = max(maxWater, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater