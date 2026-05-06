#first thoughts, bf == iterate array for every n calculate sum with every other, see if it == target O(n^2)
#can assume every input has exactly one solution
#iterate list, for each n calculate difference with target (what we need to equal target) and check if in map
#if not in map add current value to map with {val:idx} 
#if in map return [idx from map, current idx]


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:	
		map = {}
		
		for i, num in enumerate(nums):
			compliment = target - num
			if compliment in map:
				return [map[compliment], i]
			map[num] = i
		return []