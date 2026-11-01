from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Step 1: Set up pointers at both ends of the list
        left = 0
        right = len(nums) - 1

        # Step 2: Squeeze the search window until left and right meet
        while left < right:
            mid = (left + right) // 2

            # Case 1: The middle number is strictly greater than the rightmost number.
            # This means the drop (minimum) MUST be strictly in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1

            # Case 2: The middle number is smaller than or equal to the rightmost number.
            # This means the right half is sorted, so the minimum is at 'mid' or to its left.
            else:
                right = mid

        # When left == right, both pointers land exactly on the smallest number
        return nums[left]