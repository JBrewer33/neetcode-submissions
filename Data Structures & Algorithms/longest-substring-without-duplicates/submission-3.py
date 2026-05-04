class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #bc
        if len(s) < 2:
            return len(s)

        #iterate string, keep track of left, max substring, when hit duplicate move left one past update last seen map and continue iterating
        # track duplicates with a hashmap where the value is the last index

        left = 0
        maxSub = 0
        hashMap = {}

        for right in range(len(s)):

            if s[right] in hashMap:
                left = max(left, hashMap[s[right]] + 1) #left never moves backwards

            hashMap[s[right]] = right
            maxSub = max(maxSub, right - left + 1)
        
        return maxSub


#Time - O(n)
#Space - O(m) but chars are limeted to printable ascii = 96 = O(1)
        