class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Filter and collect only lowercase letters and digits
        cleaned_chars = []
        for char in s:
            if char.isalnum():
                cleaned_chars.append(char.lower())

        # Step 2: Compare characters from both ends moving inward
        left = 0
        right = len(cleaned_chars) - 1

        while left < right:
            # If characters at opposite ends don't match, it's not a palindrome
            if cleaned_chars[left] != cleaned_chars[right]:
                return False

            # Move pointers toward the center
            left += 1
            right -= 1

        # All matching pairs matched successfully
        return True