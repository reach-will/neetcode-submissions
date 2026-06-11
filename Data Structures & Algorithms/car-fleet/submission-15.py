class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))

        fleet = None
        ans = 0

        for p, s in reversed(cars):

            if fleet:
                fp, fs = fleet

                t = (target - fp) / fs

                # rear car reaches/passes target
                # before front fleet finishes
                if p + s * t >= target:
                    continue

            fleet = (p, s)
            ans += 1

        return ans