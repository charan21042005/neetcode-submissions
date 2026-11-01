from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: The search range for eating speed k
        left = 1
        right = max(piles)

        # Store the best valid speed found so far
        result = right

        # Step 2: Binary search on the speed
        while left <= right:
            speed = (left + right) // 2

            # Step 3: Calculate total hours needed at this speed
            total_hours = 0
            for pile in piles:
                # Math formula to divide and round up to the next hour:
                # (pile + speed - 1) // speed
                hours_for_pile = (pile + speed - 1) // speed
                total_hours += hours_for_pile

            # Step 4: Check if Koko finished within h hours
            if total_hours <= h:
                # Speed works! Try to find an even smaller valid speed
                result = speed
                right = speed - 1
            else:
                # Too slow! Increase the speed
                left = speed + 1

        return result