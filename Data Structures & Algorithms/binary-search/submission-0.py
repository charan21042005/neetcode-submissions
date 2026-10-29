from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Find the middle index
            mid = (left + right) // 2
            mid_val = nums[mid]

            # Case 1: Target found
            if mid_val == target:
                return mid

            # Case 2: Middle value is too big, target is in the left half
            elif mid_val > target:
                right = mid - 1

            # Case 3: Middle value is too small, target is in the right half
            else:
                left = mid + 1

        # Target does not exist in the array
        return -1