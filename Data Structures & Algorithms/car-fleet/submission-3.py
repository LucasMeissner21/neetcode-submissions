class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Attempt 1, sort target, position pair reversed, then hold a stack of finishing times. If a following
        # car's finishing time is faster, it catches up to fleet, pop it off stack, 
        # otherwise new fleet is created and stays on stack. length of stack is # fleets
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