class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(list(zip(position, speed)))
        curr_fleet = None
        ans = 0
        for f in reversed(fleets):
            if curr_fleet and (f[1] > curr_fleet[1] and f[0] + f[1] * curr_fleet[2] >= curr_fleet[0] + curr_fleet[1] * curr_fleet[2]):
                continue
            curr_fleet = (f[0], f[1], (target - f[0]) / f[1])
            ans += 1
        return ans