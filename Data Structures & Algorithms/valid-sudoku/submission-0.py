from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Step 1: Create 9 empty sets for rows, 9 for cols, 9 for boxes
        rows = []
        columns = []
        boxes = []
        for i in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        # Step 2: Check every cell on the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # If the cell is empty, skip to the next one
                if val == ".":
                    continue

                # Step 3: Find which 3x3 box we are in (0 to 8)
                box_index = (r // 3) * 3 + (c // 3)

                # Step 4: Check if the number was already seen in row, col, or box
                if val in rows[r]:
                    return False
                if val in columns[c]:
                    return False
                if val in boxes[box_index]:
                    return False

                # Step 5: Record the number in all three sets
                rows[r].add(val)
                columns[c].add(val)
                boxes[box_index].add(val)

        # If no duplicates were found across all 81 cells, the board is valid
        return True