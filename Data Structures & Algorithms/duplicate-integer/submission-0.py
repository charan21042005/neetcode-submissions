from typing import List  # For type hints

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Determine if array contains any duplicates.

        Args:
            nums: List of integers to check

        Returns:
            bool: True if duplicates found, False otherwise

        Time Complexity: O(n) average
        Space Complexity: O(n)
        """

        # Step 1: Create an empty hash set
        # Python's set provides O(1) average time for operations
        # Unlike lists, sets don't allow duplicates
        seen = set()

        # Step 2: Iterate through each number in the array
        # Python's for loop is clean and readable
        for num in nums:

            # Step 3a: Check if this number has been seen before
            # 'num in seen' is Python's membership test
            # Returns True if exists, False otherwise
            # This is very readable and expressive
            if num in seen:
                # Duplicate found! We can return immediately
                # No need to process remaining elements
                return True

            # Step 3b: Remember this number for future checks
            # seen.add(num) inserts num into the set
            # If num already exists, it does nothing (but we already checked)
            seen.add(num)

        # Step 4: We've checked all elements and found no duplicates
        # All numbers are unique
        return False