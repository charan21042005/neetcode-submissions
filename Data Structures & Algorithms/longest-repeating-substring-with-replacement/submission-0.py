class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to track counts of each letter inside our window
        counts = {}

        left = 0
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            right_char = s[right]

            # Step 1: Add the new letter to our dictionary
            if right_char in counts:
                counts[right_char] += 1
            else:
                counts[right_char] = 1

            # Step 2: Track the highest count of any single character in window
            if counts[right_char] > max_freq:
                max_freq = counts[right_char]

            # Step 3: Check how many letters we would have to replace
            window_len = right - left + 1
            replacements_needed = window_len - max_freq

            # Step 4: If we need more than k changes, shrink from the left
            if replacements_needed > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            # Step 5: Update the longest valid window length
            current_len = right - left + 1
            if current_len > longest:
                longest = current_len

        return longest