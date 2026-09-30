class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores the last seen index for each character: {char: index}
        last_seen = {}

        left = 0
        longest = 0

        for right in range(len(s)):
            current_char = s[right]

            # If current character was seen before AND is inside our current window:
            # jump 'left' directly to one position past its previous occurrence
            if current_char in last_seen and last_seen[current_char] >= left:
                left = last_seen[current_char] + 1

            # Update the character's latest position
            last_seen[current_char] = right

            # Calculate window length
            current_length = right - left + 1

            # Update best record
            if current_length > longest:
                longest = current_length

        return longest