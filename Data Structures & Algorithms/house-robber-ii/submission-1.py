class Solution:
    def rob(self, nums: List[int]) -> int:
        #arranged in circle means if we rob 0 we cannot rob n-1
        #final value will either be in n-1 if we started at 1 or n-2 if we started at 0
        #1-d dp but can optimize space by not using a dp array
        #options are rob i + 2 or i + 3
        #use two loops, one skippin the first, one skippin the last return max

        n = len(nums)
        #bc
        if n < 1:
            return 0
        if n == 1:
            return nums[0]

        rob1 = 0 #max for i-2
        rob2 = 0 #max for i-1

        for num in nums[1:]:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        
        skip1 = rob2
        rob1 = 0
        rob2 = 0

        for num in nums[:n-1]:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        
        return max(rob2, skip1)

