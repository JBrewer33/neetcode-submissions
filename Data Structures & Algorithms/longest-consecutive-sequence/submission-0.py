class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        m = defaultdict(int)
        l = 0

        for num in nums:
            if not m[num]:
                m[num] = m[num - 1] + m[num + 1] + 1 #add to map, value = itself plus count of possible consecutive numbers
                m[num - m[num-1]] = m[num]
                m[num + m[num + 1]] = m[num]
                l = max(m[num], l)
        return l
                