#find kth largest in a stream of values inc duplicates
#stream not guarenteed sorted
#duplicates still count ie. 2nd largest from [1, 2, 3, 3] == 3

class KthLargest:
	
	def __init__(self, k: int, nums: List[int]):
		self.k = k
		heapq.heapify(nums)
		while len(nums) > k:
			heapq.heappop(nums)
		self.kLargest = nums
		
	def add(self, val: int) -> int:
		if len(self.kLargest) < self.k:
			heapq.heappush(self.kLargest, val)
		else:
			heapq.heappushpop(self.kLargest, val)
		return self.kLargest[0]