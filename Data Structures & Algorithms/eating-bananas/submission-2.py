import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            # Guess the middle speed
            k = (left + right) // 2

            # Count the hours needed at speed k
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            # Case 1: speed k is fast enough
            if hours <= h:
                result = k          # remember this working speed
                right = k - 1       # try an even slower speed

            # Case 2: speed k is too slow
            else:
                left = k + 1        # we need a faster speed

        return result