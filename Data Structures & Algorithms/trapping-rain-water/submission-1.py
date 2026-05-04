class Solution:
    def trap(self, height: List[int]) -> int:
        
        #two pointer
        #start pointer at each end and work inward
        #track the max left and max right bars
        #max water depends on the shorter of the two pointers so
        #move the pointer that points to the shortest bar
        #only calculate after moving
        #calculate water with += maxSide - currentSide

        #bc
        if len(height) < 3:
            return 0
        
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0

        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
                         
            #move the lower of the two bars, recalc max for that side, calculate water at that point
            if height[left] < height[right]:
                left += 1
                leftMax = max(height[left], leftMax)
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                water += rightMax - height[right]
        
        return water
            
    #Time - iterating array at most once = O(n)
    #Space - no additional = O(1)