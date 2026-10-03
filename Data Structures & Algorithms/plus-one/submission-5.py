class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end = len(digits) - 1

        if digits[end] < 9:
            digits[end] += 1
            return digits

        while digits[end] == 9:
            if end == 0:
                digits.append(0)
                digits[end] = 1
                return digits
            
            digits[end] = 0
            end -= 1

        digits[end] += 1
        return digits