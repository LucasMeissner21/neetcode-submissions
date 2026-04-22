class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.mins) == 0 or val <= self.mins[len(self.mins) - 1]:
            self.mins.append(val)

    def pop(self) -> None:
        val = self.items.pop()
        if val == self.mins[len(self.mins) - 1]:
            self.mins.pop()

    def top(self) -> int:
        return self.items[len(self.items) - 1]

    def getMin(self) -> int:
        return self.mins[len(self.mins) - 1]
        
