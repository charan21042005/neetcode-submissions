class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies using basic if/else
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # Step 2: Turn into (frequency, number) pairs
        # By putting frequency FIRST, Python sorts by frequency automatically!
        pairs = []
        for num in counts:
            freq = counts[num]
            pairs.append((freq, num))

        # Step 3: Sort highest frequency to lowest
        pairs.sort(reverse=True)

        # Step 4: Pick the first k numbers
        result = []
        for i in range(k):
            number = pairs[i][1]
            result.append(number)

        return result