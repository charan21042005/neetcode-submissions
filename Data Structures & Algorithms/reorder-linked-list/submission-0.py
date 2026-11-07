from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Edge case: if list is empty or has only 1 node, nothing to reorder
        if head is None or head.next is None:
            return

        # ========================================================
        # STEP 1: FIND THE MIDDLE OF THE LIST (Slow & Fast)
        # ========================================================
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 'slow' is now at the midpoint.
        # Cut the list into two halves.
        second_half_head = slow.next
        slow.next = None  # End the first half

        # ========================================================
        # STEP 2: REVERSE THE SECOND HALF
        # ========================================================
        prev = None
        curr = second_half_head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 'prev' is now the head of the reversed second half
        second = prev
        first = head

        # ========================================================
        # STEP 3: ZIP THE TWO HALVES TOGETHER
        # ========================================================
        while second is not None:
            # Save the next pointers for both halves
            next_first = first.next
            next_second = second.next

            # Connect first to second
            first.next = second

            # Connect second to the rest of the first half
            second.next = next_first

            # Advance both pointers forward
            first = next_first
            second = next_second