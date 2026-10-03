from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indices of numbers.
        # Front of window_indices (index 0) will ALWAYS hold the index of the largest number.
        window_indices = deque()
        result = []

        for current_idx in range(len(nums)):
            current_num = nums[current_idx]

            # Rule 1: Drop indices that slid out of the window frame on the left
            oldest_allowed_idx = current_idx - k + 1
            while len(window_indices) > 0 and window_indices[0] < oldest_allowed_idx:
                window_indices.popleft()

            # Rule 2: Remove smaller numbers from the back.
            # If current_num is greater than or equal to an older number in the queue,
            # that older number can never be the maximum again.
            while len(window_indices) > 0 and nums[window_indices[-1]] <= current_num:
                window_indices.pop()

            # Rule 3: Add current index to the back of the queue
            window_indices.append(current_idx)

            # Rule 4: Once our window reaches size k, the front element is our maximum
            if current_idx >= k - 1:
                max_idx = window_indices[0]
                result.append(nums[max_idx])

        return result