from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack stores pairs of: (start_index, height)
        stack = []
        max_area = 0

        # Loop through every bar (plus an extra 0 at the end to flush the stack)
        for i in range(len(heights) + 1):
            # If we reached the end, use height 0 to pop all remaining bars
            if i < len(heights):
                current_height = heights[i]
            else:
                current_height = 0

            # The current bar starts at index i by default
            start_index = i

            # While stack is not empty and the current bar is shorter than the bar on top of stack
            while len(stack) > 0 and stack[-1][1] > current_height:
                # Pop the taller bar
                popped_start_idx, popped_height = stack.pop()

                # Calculate the area formed using the popped bar's height
                width = i - popped_start_idx
                area = popped_height * width

                # Update maximum area
                if area > max_area:
                    max_area = area

                # The current shorter bar could have extended backwards to where the popped bar started
                start_index = popped_start_idx

            # Push the current bar with its furthest-back start index
            stack.append((start_index, current_height))

        return max_area