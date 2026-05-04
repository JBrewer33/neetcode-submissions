class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s - 0<=len(s)<=1000 - all ascii
        #find longest substring with no duplicate chars
        #brute force - for each char walk until you find duplicate, count
        #sliding window, iterate string, track left of window, track max window size, update when finding dupe
        #   need way to track duplicates - set or hashmap

        #bc
        if len(s) < 2:
            return len(s)
        
        left = 0
        maxSub = 0
        hmap = {}

        for right in range(len(s)):

            if s[right] in hmap:
                left = max(left, hmap[s[right]] + 1)#if in map update left to one index forward from its last occurance (never backward)
            hmap[s[right]] = right
            maxSub = max(maxSub, right - left + 1)
            
        return maxSub
            



        