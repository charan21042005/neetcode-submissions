from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize previous pointer as None
        prev = None
        curr = head

        # Step 2: Iterate through every node in the list
        while curr is not None:
            # Save the next node so we don't lose the rest of the list
            next_node = curr.next

            # Reverse the pointer: point backwards to previous node
            curr.next = prev

            # Advance 'prev' and 'curr' one step forward
            prev = curr
            curr = next_node

        # When curr becomes None, prev points to the new head
        return prev