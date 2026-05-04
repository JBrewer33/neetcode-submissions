class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #treat list as stack
        #pop values one a time recording the minumum value and calulating maximum profit with curr - min

        minVal = prices[0]
        maxProfit = 0

        for price in prices:
            minVal = min(minVal, price)
            maxProfit = max(maxProfit, price - minVal)
        
        return maxProfit
        

#Time - at most iterate list once = O(n)
#Space - no extra data structs = O(1)