class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #every step have 2 options, take 1 step or 2 steps - same cost
        #want to do 1-d dp where answer is at end of array and every entry is the number of options up to that point
        #need to manually initilize idx 0,1

        if len(cost) < 2:
            return 0

        #because we can start on 0 or 1 we start the loop on 2
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2]) #calculate the min cost at step

        return min(cost[len(cost) - 1], cost[len(cost) - 2]) 

