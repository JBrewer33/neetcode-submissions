class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right-1) // 2

            if target <= nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1

        return left if (left < len(nums) and nums[left] == target) else -1
            

        
