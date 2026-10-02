class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is longer than s, impossible to contain all letters
        if len(t) > len(s):
            return ""

        # Step 1: Count how many of each letter we need from t
        target_counts = {}
        for char in t:
            if char in target_counts:
                target_counts[char] += 1
            else:
                target_counts[char] = 1

        # Step 2: Trackers for sliding window
        window_counts = {}
        letters_needed = len(target_counts)   # Number of unique characters to satisfy
        letters_satisfied = 0                # How many unique characters currently meet the requirement

        left = 0
        min_len = len(s) + 1                 # Any number bigger than len(s) works as "infinity"
        best_left = 0
        best_right = 0

        # Step 3: Expand the window with right pointer
        for right in range(len(s)):
            right_char = s[right]

            # Add character to window counts
            if right_char in window_counts:
                window_counts[right_char] += 1
            else:
                window_counts[right_char] = 1

            # Check if this character now meets the required frequency
            if right_char in target_counts:
                if window_counts[right_char] == target_counts[right_char]:
                    letters_satisfied += 1

            # Step 4: When all required characters are satisfied, shrink from left
            while letters_satisfied == letters_needed:
                current_len = right - left + 1

                # If this window is smaller than our previous best, save its boundaries
                if current_len < min_len:
                    min_len = current_len
                    best_left = left
                    best_right = right

                # Remove the leftmost character as we shrink
                left_char = s[left]
                window_counts[left_char] -= 1

                # If removing it breaks the requirement, decrement satisfied count
                if left_char in target_counts:
                    if window_counts[left_char] < target_counts[left_char]:
                        letters_satisfied -= 1

                # Move left pointer forward
                left += 1

        # If min_len was never updated, no valid window was found
        if min_len > len(s):
            return ""

        # Slice and return the smallest valid window
        return s[best_left : best_right + 1]