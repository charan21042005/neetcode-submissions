# Definition of a Doubly Linked List Node
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Maps key -> Node
        self.cache = {}

        # Dummy nodes to mark boundaries
        # self.left = LRU (Least Recently Used)
        # self.right = MRU (Most Recently Used)
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Connect dummy nodes: left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    # Helper 1: Remove a node from anywhere in the doubly linked list
    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper 2: Insert a node right before self.right (MRU position)
    def insert(self, node: Node) -> None:
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Since it was accessed, move it to the MRU position (right end)
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove the old node first
        if key in self.cache:
            self.remove(self.cache[key])

        # Create the new node and insert it at the MRU position
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # If cache exceeds capacity, evict the least recently used node (at left)
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]