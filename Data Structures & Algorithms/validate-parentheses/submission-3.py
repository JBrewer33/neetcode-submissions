class Solution:
	def isValid(self, s: str) -> bool:
		if len(s) < 1:
			return True
		if len(s) < 2:
			return False

		stack = deque()
		map = {'(':"open", '{':"open", '[':"open"}
		
		for char in s:
			if char in map and map[char] == "open":
				stack.append(char)
			else:
				if not stack:
					return False
				temp = stack.pop()
				if char == ')' and temp != '(':
					return False
				if char == ']' and temp != '[':
					return False
				if char == '}' and temp != '{':
					return False
		return True and not stack