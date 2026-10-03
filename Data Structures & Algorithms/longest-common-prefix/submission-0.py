class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ret = list(strs[0])
        length = len(ret)
        for i in range(1, len(strs)):
            while length != 0 and ret != list(strs[i][:length]):
                ret.pop()
                length -= 1
            if length == 0:
                return ""
        return "".join(ret)