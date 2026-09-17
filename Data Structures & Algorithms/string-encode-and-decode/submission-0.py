class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Step 1: Find where '#' is located starting from index i
            hash_index = s.find('#', i)

            # Step 2: Everything before '#' is the length of the next word
            length = int(s[i:hash_index])

            # Step 3: The actual word begins right after '#'
            start = hash_index + 1
            word = s[start : start + length]

            # Step 4: Add the word to our result
            result.append(word)

            # Step 5: Jump pointer to the next encoded block
            i = start + length

        return result
