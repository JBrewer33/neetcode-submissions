class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return [min(seen[comp], i), max(seen[comp], i)]
            seen[nums[i]] = i
        return []