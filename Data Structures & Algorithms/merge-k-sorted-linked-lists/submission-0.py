from typing import List, Optional

# Definition for singly-linked list node:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Step 1: Handle empty input edge case
        if not lists or len(lists) == 0:
            return None

        # Step 2: Keep pairing and merging lists until only 1 list remains
        while len(lists) > 1:
            merged_lists = []

            # Jump by 2 each step to grab pairs: (0, 1), (2, 3), etc.
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                
                # Check if a second list exists in this pair (handles odd number of lists)
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None

                # Merge the pair using our standard 2-list merge helper
                combined = self.mergeTwoLists(list1, list2)
                merged_lists.append(combined)

            # Replace old lists with the newly merged half-sized list of lists
            lists = merged_lists

        # Step 3: Return the single final merged list
        return lists[0]

    # Helper function: Exact same code from "Merge Two Sorted Lists"
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is not None:
            tail.next = list1
        elif list2 is not None:
            tail.next = list2

        return dummy.next