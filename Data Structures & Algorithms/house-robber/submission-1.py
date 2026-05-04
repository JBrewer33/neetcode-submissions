class Solution:
    def rob(self, nums: List[int]) -> int:
        #no adjacent, maximum you can get with no adj
        #no technical limits on skipped spots but there is no reason to skip more than 2 to maximize
        #so our recursion decision should be do we take i+2, i+3
        #by the same logic we should start at either i = 0 or 1 so we should start loop on 3 but need to manually update 2
        #this should be 1-d dp so we can save space by modifying nums in place
        #number should be in n - 1 or n - 2
        #bc num houses < 1 return 0
        n = len(nums)
        if n < 1:
            return 0

        #to avoid out of range have to manually update i = 2 to include i = 0
        if n > 2:
            nums[2] += nums[0]

        for i in range(3, n):
            nums[i] += max(nums[i-2], nums[i-3])
        
        return max(nums[n-1], nums[n-2])