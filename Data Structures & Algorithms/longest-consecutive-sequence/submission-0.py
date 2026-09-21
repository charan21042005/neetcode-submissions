from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Check if the input list is completely empty
        if len(nums) == 0:
            return 0

        # Convert the list into a set for instant O(1) lookups
        numbers = set(nums)
        longest = 0

        # Loop through every unique number
        for num in numbers:
            # Check if this number is the beginning of a sequence
            # If (num - 1) is already in the set, this is NOT the start
            if (num - 1) not in numbers:
                current_num = num
                current_length = 1

                # Keep counting as long as the consecutive next numbers exist
                while (current_num + 1) in numbers:
                    current_num += 1
                    current_length += 1

                # Update the longest length found so far
                if current_length > longest:
                    longest = current_length

        return longest