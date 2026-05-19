#push numbers to stack, when hitting a opperator pop and evaluate

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(int(first / second))
        return stack.pop()