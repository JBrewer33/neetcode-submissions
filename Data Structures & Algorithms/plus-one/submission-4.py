class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end = len(digits) - 1

        if digits[end] < 9:
            digits[end] += 1
            return digits

        while digits[end] == 9:
            if end == 0:
                ret = [0] * (len(digits) + 1)
                ret[0] += 1
                return ret
            
            digits[end] = 0
            end -= 1

        digits[end] += 1
        return digits