class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(list(zip(position, speed)), reverse=True)
        curr_fleet = fleets[0]
        ans = 1
        for f in fleets[1:]:
            if f[1] > curr_fleet[1] and (target - curr_fleet[0]) / curr_fleet[1] >= (target - f[0]) / f[1]:
                continue
            curr_fleet = f
            ans += 1
        return ans