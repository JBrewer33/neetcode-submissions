class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k == 0:
            return None

        heapq.heapify(nums) #turns nums into min heap

        while len(nums) > k:
            heapq.heappop(nums) #pop the minimum element from the heap until size == k meaning heap[0] == kth largest
        
        return nums[0]