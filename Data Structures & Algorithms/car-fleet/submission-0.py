from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Pair each car's position with its speed
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # Step 2: Sort cars by position in descending order (closest to target first)
        cars.sort(reverse=True)

        # Step 3: Use a stack to track the arrival times of fleet leaders
        fleet_times = []

        # Step 4: Calculate time for each car
        for pos, spd in cars:
            distance_left = target - pos
            time_to_reach = distance_left / spd

            # If this car takes longer than the fleet ahead of it,
            # it cannot catch up, so it becomes the leader of a new fleet.
            if len(fleet_times) == 0 or time_to_reach > fleet_times[-1]:
                fleet_times.append(time_to_reach)
            
            # If time_to_reach <= fleet_times[-1], this car catches up
            # to the fleet ahead and merges with it, so we do nothing!

        # The number of fleet arrival times in the stack is our answer
        return len(fleet_times)