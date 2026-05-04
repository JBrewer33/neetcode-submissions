class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False