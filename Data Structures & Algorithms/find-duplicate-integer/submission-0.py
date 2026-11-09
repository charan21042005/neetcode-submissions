from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Initialize two pointers at the start
        slow = 0
        fast = 0

        # Phase 1: Detect that a cycle exists and find the meeting point
        while True:
            # Slow moves 1 step: index -> nums[index]
            slow = nums[slow]
            
            # Fast moves 2 steps: index -> nums[nums[index]]
            fast = nums[nums[fast]]

            # When they collide, break out of Phase 1
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (the duplicate number)
        slow2 = 0
        while True:
            # Both pointers move 1 step at a time
            slow = nums[slow]
            slow2 = nums[slow2]

            # The node where they meet is the duplicate number!
            if slow == slow2:
                return slow