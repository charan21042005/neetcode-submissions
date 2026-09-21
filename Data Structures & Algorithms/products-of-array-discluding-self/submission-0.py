from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
      
        # Create prefix array
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
      
        # Create suffix array
        suffix = [1] * n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
      
        # Combine
        output = [1] * n
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
      
        return output