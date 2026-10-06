class MinStack:
    def __init__(self):
        # Stack 1: Holds the actual pushed values
        self.stack = []
        # Stack 2: Tracks the minimum value at each level
        self.min_stack = []

    def push(self, val: int) -> None:
        # Always push the number onto the main stack
        self.stack.append(val)

        # If min_stack is empty, this number is automatically our minimum
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            # Current minimum is the smaller between new val and previous minimum
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:
        # Both stacks must pop together to stay in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Returns the most recently added number from the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # The top of min_stack is ALWAYS the minimum of the entire main stack
        return self.min_stack[-1]