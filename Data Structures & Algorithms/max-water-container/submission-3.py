class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        #bc 1 or less in list
        if r < 1:
            return 0
        a = 0
        
        #iterate until pointers meet
        while l < r:
            a = max(a, min(heights[l], heights[r]) * (r - l)) #calculate max area with current pointers (lower of two bars * base)
            
            #move the pointer for the shorter of the two bars
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return a        
