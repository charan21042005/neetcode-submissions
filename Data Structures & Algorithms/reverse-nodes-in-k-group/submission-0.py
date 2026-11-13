from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node pointing to head
        dummy = ListNode(0)
        dummy.next = head

        # 'group_prev' always points to the node right BEFORE the current k-group
        group_prev = dummy

        while True:
            # Step 2: Check if there are at least k nodes left to reverse
            kth_node = self.getKthNode(group_prev, k)
            if kth_node is None:
                break

            # Save the node right AFTER the current k-group
            group_next = kth_node.next

            # Step 3: Reverse the k nodes in the current group
            # Start 'prev' at 'group_next' so the first node (which becomes the tail)
            # automatically links to the next group!
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Step 4: Connect the previous part of the list to the newly reversed group
            # Before reversal, group_prev.next was the first node of the group.
            # After reversal, it is now the LAST node of the group!
            old_group_head = group_prev.next
            group_prev.next = kth_node

            # Advance 'group_prev' to the end of this reversed group for the next round
            group_prev = old_group_head

        return dummy.next

    # Helper function to walk k steps forward from 'curr'
    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr is not None and k > 0:
            curr = curr.next
            k -= 1
        return curr