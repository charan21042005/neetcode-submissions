class Solution:
    def isValid(self, s: str) -> bool:
        # Step 1: Create an empty stack to remember open brackets
        stack = []

        # Step 2: Loop through each bracket in the string
        for char in s:
            # Case 1: If it's an opening bracket, push it onto the stack
            if char == "(" or char == "{" or char == "[":
                stack.append(char)

            # Case 2: If it's a closing bracket
            else:
                # If stack is empty, there is no opening bracket to match
                if len(stack) == 0:
                    return False

                # Peek at the most recently opened bracket
                top = stack[-1]

                # Check if current closing bracket matches the top opening bracket
                if char == ")" and top != "(":
                    return False
                if char == "}" and top != "{":
                    return False
                if char == "]" and top != "[":
                    return False

                # If it matched, remove that opening bracket from the stack
                stack.pop()

        # Step 3: If stack is empty, all brackets were matched properly
        if len(stack) == 0:
            return True
        else:
            return False