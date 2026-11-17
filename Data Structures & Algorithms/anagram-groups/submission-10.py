class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for s in strs:
            sortedList = sorted(list(s))
            sortedString = "".join(sortedList)
            if sortedString in anagrams:
                anagrams[sortedString].append(s)
            else:
                anagrams[sortedString] = [s]

        
        ret = []

        for anagram in anagrams:
            ret.append(anagrams[anagram])

        return ret