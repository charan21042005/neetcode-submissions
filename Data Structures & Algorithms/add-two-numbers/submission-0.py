from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to anchor our result list
        dummy = ListNode(0)
        tail = dummy

        # Step 2: Track carry-over value between columns
        carry = 0

        # Step 3: Loop while there are digits left in l1, l2, or a remaining carry
        while l1 is not None or l2 is not None or carry > 0:
            digit1 = 0
            if l1 is not None:
                digit1 = l1.val
                l1 = l1.next

            digit2 = 0
            if l2 is not None:
                digit2 = l2.val
                l2 = l2.next

            # Sum digits and carry
            column_sum = digit1 + digit2 + carry

            # Calculate new carry and the single digit to store
            carry = column_sum // 10
            new_digit = column_sum % 10

            # Attach new node to the merged result list
            tail.next = ListNode(new_digit)
            tail = tail.next

        # Step 4: The result list starts right after the dummy node
        return dummy.next