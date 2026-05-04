class Solution:
    def longestPalindrome(self, s: str) -> str:
        #interate the string, take each letter as the potential middle of a palindrome, recurse on left and right
        #each step, is left == right, if palindrom is even length 2 middle chars will be equal
        #so if left == right expand both outward or left == middle or right == middle expand just the one that equals mid
        #since we need to return the actual palandrome build palindrome strings and save at middle index - requires array can probably just do with pointers
        #actually if we save the length at the middle index we can return the substring directly through calculation
        
        if len(s) == 1:
            return s
        
        maxLen = 0#len of largest found pal
        maxIdx = 0#starting idx of largest found pal
        left = 0
        right = 0
        
        for i in range( len(s)-1):
            
            #odd
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    maxIdx = left
                left -= 1
                right += 1

            #even
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    maxIdx = left
                left -= 1
                right += 1
            if maxLen == len(s):
                return s
        return s[maxIdx:maxIdx+maxLen] 

#Time - 
           
            
            

