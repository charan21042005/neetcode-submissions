from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Step 1: Check if target is at mid
            if nums[mid] == target:
                return mid

            # Step 2: Check if the left half is normally sorted
            if nums[left] <= nums[mid]:
                # Is target within the sorted left half?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Step 3: Otherwise, the right half must be normally sorted
            else:
                # Is target within the sorted right half?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target not found in the array
        return -1