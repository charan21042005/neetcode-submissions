from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # Case 1: Addition
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)

            # Case 2: Subtraction
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)

            # Case 3: Multiplication
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)

            # Case 4: Division (truncated toward zero)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                # int(first / second) truncates toward zero properly in Python
                result = int(first / second)
                stack.append(result)

            # Case 5: It is a number
            else:
                stack.append(int(token))

        # The last remaining item in the stack is the final result
        return stack[0]