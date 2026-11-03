class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #2 ways
        #store compliment, for each loop check if num in map, if so return if not calc compliment and add
        #store number for each cal compliment check if in map if not add number to map
        comps = {}
        for i, num in enumerate(nums):
            if num in comps:
                return [comps[num], i]
            comp = target - num
            comps[comp] = i
        return False

