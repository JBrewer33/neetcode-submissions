class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) < 2:
            return False
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False