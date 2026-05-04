class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #treat list as stack
        #pop values one a time recording the minumum value and calulating maximum profit with curr - min

        top = len(prices) - 1
        maxVal = 0
        maxProfit = 0
        
        while top >= 0:
            maxProfit = max(maxVal - prices[top], maxProfit)
            maxVal = max(prices[top], maxVal)
            top -= 1

        #can choose not to buy so min profit == 0    
        return maxProfit

#Time - at most iterate list once = O(n)
#Space - no extra data structs = O(1)