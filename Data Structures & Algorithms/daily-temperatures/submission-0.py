class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = len(temperatures)
        res = [0] * t
        stack = []
        stack.append([temperatures[0], 0])

        for i in range(1, t):
            temp = temperatures[i]
            j = len(stack) - 1
            if temp < stack[j][0]:
                stack.append([temp, i])
            else:
                while stack and temp > stack[j][0]:
                    index = stack[j][1]
                    curr = stack.pop()
                    res[index] = i - curr[1]
                    j = len(stack) - 1
                stack.append([temp, i])
        return res
