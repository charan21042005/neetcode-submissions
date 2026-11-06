from typing import Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Create a dummy node to act as the head of our new list
        dummy = ListNode(0)
        
        # 'tail' will always point to the last node in our merged list
        tail = dummy

        # Step 2: Compare nodes from both lists while neither is empty
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # Attach list1's node
                tail.next = list1
                # Advance list1 to its next node
                list1 = list1.next
            else:
                # Attach list2's node
                tail.next = list2
                # Advance list2 to its next node
                list2 = list2.next

            # Move our tail pointer forward
            tail = tail.next

        # Step 3: Attach whichever list still has remaining nodes
        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2

        # Step 4: The real head is the node directly after our dummy node
        return dummy.next