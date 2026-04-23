class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Second attempt, dynamic programming, move backwards through temperatures and check next day for warmer
        # if next day is colder, move forward until day that is warmer than next or end of list
        # if valid day is found, set result to jth day - ith day
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            if j < n:
                res[i] = j - i
        return res
