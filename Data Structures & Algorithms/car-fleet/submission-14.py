class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))

        fleet = None
        ans = 0

        for p, s in reversed(cars):

            if fleet:
                fp, fs = fleet

                # catches fleet before target
                if (
                    s > fs and
                    (fp - p) * fs <= (target - fp) * (s - fs)
                ):
                    continue

            fleet = (p, s)
            ans += 1

        return ans