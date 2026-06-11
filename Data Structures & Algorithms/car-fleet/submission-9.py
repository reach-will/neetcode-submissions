class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(list(zip(position, speed)))
        curr_fleet_time = 0
        ans = 0
        for f in reversed(fleets):
            time_to_target = (target - f[0]) / f[1]
            if time_to_target > curr_fleet_time:
                ans += 1
                curr_fleet_time = time_to_target
        return ans