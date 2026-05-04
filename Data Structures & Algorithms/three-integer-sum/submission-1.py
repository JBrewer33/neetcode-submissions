class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i, num in enumerate(nums):
            if num > 0:#break as everything else will be > 0
                return ret
            if i > 0 and num == nums[i-1]: #skip dupes
                continue
            
            f = i + 1 # front starts num + 1
            b = len(nums) - 1 #back starts at end
            while f < b:
                tsum = num + nums[f] + nums[b] #current tripple sum
                if tsum == 0:
                    ret.append([num, nums[f], nums[b]])
                    f += 1
                    b -= 1
                    while nums[f] == nums[f-1] and f < b:
                        f += 1
                elif tsum > 0:
                    b -= 1
                elif tsum < 0:
                    f += 1
        return ret