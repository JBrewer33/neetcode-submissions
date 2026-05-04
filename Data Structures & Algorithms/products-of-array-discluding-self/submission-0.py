class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = nums
        prod = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero += 1
                if zero > 1:
                   z = [0] * len(nums)
                   return z
                else : continue
            prod *= num
        for i in range(len(nums)):
            if res[i] == 0:
                res[i] = prod
                continue
            elif zero == 1:
                res[i] = 0
            else:
                res[i] = int(prod * pow(nums[i], -1))
        return res