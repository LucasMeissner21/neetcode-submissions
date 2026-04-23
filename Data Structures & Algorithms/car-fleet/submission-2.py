class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Attempt 1, sort target, position pair reversed, then hold a stack of finishing times. If a following
        # car's finishing time is faster, it catches up to fleet, pop it off stack, 
        # otherwise new fleet is created and stays on stack. length of stack is # fleets
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        stack = []
        for p, s in pair:
            stack.append((target - p) / s) # finish time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)