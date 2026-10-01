class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, s2 can't contain a permutation of s1
        if len(s1) > len(s2):
            return False

        # Step 1: Count character frequencies for s1
        target_counts = {}
        for char in s1:
            if char in target_counts:
                target_counts[char] += 1
            else:
                target_counts[char] = 1

        # Step 2: Set up a window of size len(s1)
        window_counts = {}
        k = len(s1)

        # Count the characters in the first window of s2 (from index 0 to k - 1)
        for i in range(k):
            char = s2[i]
            if char in window_counts:
                window_counts[char] += 1
            else:
                window_counts[char] = 1

        # Check if the very first window is already an exact match
        if window_counts == target_counts:
            return True

        # Step 3: Slide the window one character at a time across the rest of s2
        for i in range(k, len(s2)):
            new_char = s2[i]          # Character entering the window on the right
            old_char = s2[i - k]      # Character exiting the window on the left

            # Add the new character into the window counts
            if new_char in window_counts:
                window_counts[new_char] += 1
            else:
                window_counts[new_char] = 1

            # Remove or decrement the old character leaving the window
            if window_counts[old_char] == 1:
                del window_counts[old_char]
            else:
                window_counts[old_char] -= 1

            # Check if current window matches s1's character counts
            if window_counts == target_counts:
                return True

        return False