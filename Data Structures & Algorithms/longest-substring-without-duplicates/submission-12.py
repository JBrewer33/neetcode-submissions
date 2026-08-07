class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 1:
            return 0


        found = {}
        found[s[0]] = 0
        left = 0
        right = 1
        maxS = 1


        #iterate s, for each char check if already in map, if so move left pointer to previous occurance idx + 1
        #every loop, add/update char to map with (key=char, value=index) so char idx is always most "recent" occurance
        #update max
        #increment
        while right < len(s):
            if s[right] in found and found[s[right]] + 1 > left:
                left = found[s[right]] + 1
            found[s[right]] = right
            maxS = max(maxS, right - left + 1)
            right += 1
        
        return maxS


        

