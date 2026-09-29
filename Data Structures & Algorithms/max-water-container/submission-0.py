from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start pointers at both far ends
        left = 0
        right = len(heights) - 1
        
        best_water = 0

        while left < right:
            # Step 1: Distance between the two lines
            width = right - left

            # Step 2: Water level is limited by the shorter line
            if heights[left] < heights[right]:
                shorter_height = heights[left]
            else:
                shorter_height = heights[right]

            # Step 3: Calculate water area for current pair
            current_water = width * shorter_height

            # Step 4: Record if this is the largest container seen so far
            if current_water > best_water:
                best_water = current_water

            # Step 5: Always abandon the shorter line to search for a taller one
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best_water