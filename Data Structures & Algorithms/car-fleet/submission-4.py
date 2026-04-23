class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Attempt 2, Remove stack and use variables to track most recent fleet finish time and num fleets
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        prevTime = (target - pair[0][0]) / pair[0][1]
        fleets = 1
        for p, s in pair:
            currentTime = (target - p) / s
            if currentTime > prevTime:
                fleets += 1
                prevTime = currentTime

        return fleets