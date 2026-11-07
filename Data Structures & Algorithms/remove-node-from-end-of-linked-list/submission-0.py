from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node pointing to the head
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: Initialize both pointers at dummy
        left = dummy
        right = dummy

        # Step 3: Advance 'right' pointer forward by n steps
        for _ in range(n):
            right = right.next

        # Step 4: Move both pointers together until 'right' is at the last node
        while right.next is not None:
            left = left.next
            right = right.next

        # Step 5: Delete the target node by skipping it
        left.next = left.next.next

        # Step 6: Return the real head
        return dummy.next