class Solution:
    def trap(self, height: List[int]) -> int:
        #bc
        if len(height) < 3:
            return 0



        left = 0
        right = len(height) - 1
        water = 0
        maxLeft = height[left]
        maxRight = height[right]

        #start pointer on each end, calcutate the maxWater, move the pointer to the shorter bar in
        #every time we move a pointer we want to subtract the new height from the maxWater and then calculate new max
        #water == min of the two bars multiplied by distance between bars (difference between pointers)

        while left < right:

            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
            
        return water