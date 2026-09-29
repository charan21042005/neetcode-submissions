from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.

        Args:
            nums: List of integers

        Returns:
            List[List[int]]: All unique triplets summing to zero

        Time Complexity: O(n²)
        Space Complexity: O(1) extra (excluding output)
        """

        # Result list to store triplets
        result = []

        # ============================================
        # STEP 1: SORT THE ARRAY
        # ============================================

        # Enables two pointers and duplicate detection
        nums.sort()

        n = len(nums)

        # ============================================
        # STEP 2: FIX THE FIRST NUMBER
        # ============================================

        for i in range(n):

            # ============================================
            # STEP 3: SKIP DUPLICATE FIXED VALUES
            # ============================================

            # Skip if same as previous value
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # ============================================
            # STEP 4: INITIALIZE TWO POINTERS
            # ============================================

            left = i + 1
            right = n - 1

            # ============================================
            # STEP 5: TWO POINTER SEARCH
            # ============================================

            while left < right:

                # Calculate triplet sum
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # Sum too small → need larger → move left
                    left += 1

                elif total > 0:
                    # Sum too large → need smaller → move right
                    right -= 1

                else:
                    # ============================================
                    # FOUND A TRIPLET
                    # ============================================

                    # Add to result
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result