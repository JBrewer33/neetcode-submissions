class Solution:
	def isValid(self, s: str) -> bool:
		map = {'(':')', '[':']', '{':'}'}
		stack = deque()


		for c in s:
			if c in map.keys(): #push every open to stack
				stack.append(c)
			else: #when we find a close, pop stack and check if open maps to close, if not == False
				if not stack:
					return False
				check = stack.pop()
				if map[check] != c:
					return False
		
		return len(stack) == 0