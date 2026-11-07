from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Step 1: Initialize two pointers starting at the head
        slow = head
        fast = head

        # Step 2: Move pointers while fast can safely advance two steps
        while fast is not None and fast.next is not None:
            # Slow moves 1 step
            slow = slow.next
            
            # Fast moves 2 steps
            fast = fast.next.next

            # If both pointers meet at the exact same node, a cycle exists
            if slow == fast:
                return True

        # If fast reached None, there is no cycle
        return False