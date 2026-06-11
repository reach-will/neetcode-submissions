class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(list(zip(position, speed)))
        print(fleets)
        curr_fleet = None
        ans = 0
        for f in reversed(fleets):
            print(f)
            print(curr_fleet)
            print((target - f[0]) // f[1])
            print((target - curr_fleet[0]) // curr_fleet[1] if curr_fleet else None)
            print(f[0] + f[1] * (target - curr_fleet[0]) // curr_fleet[1] if curr_fleet else None)
            print(curr_fleet[0] + curr_fleet[1] * (target - curr_fleet[0]) // curr_fleet[1] if curr_fleet else None)
            print()
            print("========")
            if curr_fleet and (f[1] > curr_fleet[1] and f[0] + f[1] * (target - curr_fleet[0]) // curr_fleet[1] >= curr_fleet[0] + curr_fleet[1] * (target - curr_fleet[0]) // curr_fleet[1]):
                continue
            curr_fleet = (f[0], f[1], (target - f[0]) // f[1])
            ans += 1
        return ans