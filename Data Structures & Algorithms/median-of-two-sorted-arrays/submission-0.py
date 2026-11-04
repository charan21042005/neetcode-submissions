from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Always binary search on the shorter array
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total_length = len(A) + len(B)
        total_left = (total_length + 1) // 2

        # Binary search range for how many elements to take from A (from 0 to len(A))
        left = 0
        right = len(A)

        while left <= right:
            # i = elements taken from A
            # j = elements taken from B
            i = (left + right) // 2
            j = total_left - i

            # Boundary values for A
            if i > 0:
                A_left = A[i - 1]
            else:
                A_left = float("-inf")

            if i < len(A):
                A_right = A[i]
            else:
                A_right = float("inf")

            # Boundary values for B
            if j > 0:
                B_left = B[j - 1]
            else:
                B_left = float("-inf")

            if j < len(B):
                B_right = B[j]
            else:
                B_right = float("inf")

            # Check if partition is valid
            if A_left <= B_right and B_left <= A_right:
                # Odd total length: median is the maximum of the left side
                if total_length % 2 != 0:
                    if A_left > B_left:
                        return float(A_left)
                    else:
                        return float(B_left)

                # Even total length: average of max(left) and min(right)
                else:
                    max_left = A_left if A_left > B_left else B_left
                    min_right = A_right if A_right < B_right else B_right
                    return (max_left + min_right) / 2.0

            # A contributed too many elements to the left half
            elif A_left > B_right:
                right = i - 1

            # A contributed too few elements to the left half
            else:
                left = i + 1