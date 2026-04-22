class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        # If no min established or new value is new minimum, add to min stack
        if len(self.mins) == 0 or val <= self.mins[len(self.mins) - 1]:
            self.mins.append(val)

    def pop(self) -> None:
        val = self.items.pop()
        # Since items and mins push in the same order, popped value can only be most recent minimum or non min
        if val == self.mins[len(self.mins) - 1]:
            self.mins.pop()

    def top(self) -> int:
        return self.items[len(self.items) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]
        
