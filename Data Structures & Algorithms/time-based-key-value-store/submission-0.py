class TimeMap:
    def __init__(self):
        # A dictionary where each key maps to a list of (timestamp, value) pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is new, initialize it with an empty list
        if key not in self.store:
            self.store[key] = []
        
        # Append the new pair (timestamps arrive in ascending order)
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If key was never added, return empty string
        if key not in self.store:
            return ""

        history = self.store[key]
        
        # Binary search to find the largest timestamp <= queried timestamp
        left = 0
        right = len(history) - 1
        best_value = ""

        while left <= right:
            mid = (left + right) // 2
            mid_time, mid_val = history[mid]

            # Case 1: Exact timestamp match found
            if mid_time == timestamp:
                return mid_val

            # Case 2: This timestamp is valid (<= queried timestamp)
            elif mid_time < timestamp:
                # Save this value as our best answer so far
                best_value = mid_val
                # Try to search right to find an even closer (larger) timestamp
                left = mid + 1

            # Case 3: Timestamp is too large, search left
            else:
                right = mid - 1

        return best_value