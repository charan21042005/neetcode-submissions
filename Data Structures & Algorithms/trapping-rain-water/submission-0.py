from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Pointers starting at both ends
        left = 0
        right = len(height) - 1

        # Track the tallest wall seen so far from each direction
        left_max = 0
        right_max = 0

        total_water = 0

        while left < right:
            # Case 1: The left side is shorter or equal to the right side
            if height[left] <= height[right]:
                # If current bar is as tall as or taller than left_max, update wall
                if height[left] >= left_max:
                    left_max = height[left]
                # Otherwise, water is trapped above this bar
                else:
                    trapped = left_max - height[left]
                    total_water += trapped
                
                left += 1

            # Case 2: The right side is strictly shorter
            else:
                # If current bar is as tall as or taller than right_max, update wall
                if height[right] >= right_max:
                    right_max = height[right]
                # Otherwise, water is trapped above this bar
                else:
                    trapped = right_max - height[right]
                    total_water += trapped
                
                right -= 1

        return total_water