from typing import Optional

# Definition for a Node:
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Step 1: Base case - if original list is empty, return None
        if head is None:
            return None

        # Step 2: Hash map to store mapping: {original_node: cloned_node}
        # Pre-populate None so that old_to_new[None] cleanly returns None
        old_to_new = {None: None}

        # Step 3: Pass 1 - Create cloned nodes without wiring pointers yet
        curr = head
        while curr is not None:
            cloned_node = Node(curr.val)
            old_to_new[curr] = cloned_node
            curr = curr.next

        # Step 4: Pass 2 - Wire up .next and .random pointers for each clone
        curr = head
        while curr is not None:
            cloned_node = old_to_new[curr]
            
            # Connect the clone's next to the clone of curr.next
            cloned_node.next = old_to_new[curr.next]
            
            # Connect the clone's random to the clone of curr.random
            cloned_node.random = old_to_new[curr.random]

            curr = curr.next

        # Step 5: Return the cloned head
        return old_to_new[head]