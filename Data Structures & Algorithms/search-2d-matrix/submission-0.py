from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Step 1: Get grid dimensions
        rows = len(matrix)
        cols = len(matrix[0])

        # Step 2: Binary search boundaries over the flattened length
        left = 0
        right = (rows * cols) - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index 'mid' into 2D coordinates (row, col)
            row = mid // cols
            col = mid % cols
            mid_val = matrix[row][col]

            # Case 1: Match found
            if mid_val == target:
                return True

            # Case 2: Middle value is too big -> search left half
            elif mid_val > target:
                right = mid - 1

            # Case 3: Middle value is too small -> search right half
            else:
                left = mid + 1

        # Target not present in the matrix
        return False