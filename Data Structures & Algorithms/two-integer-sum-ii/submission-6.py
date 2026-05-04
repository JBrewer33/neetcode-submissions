class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        while front < back:
            cur = numbers[front] + numbers[back]
            if cur == target:
                return [front+1, back+1]
            elif cur > target:
                back -= 1
            elif cur < target:
                front += 1
            
