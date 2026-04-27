class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution 2: Greedy, get max frequency among tasks, then see if idle slots are
        # filled by other tasks and return result accordingly

        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        freq.sort()
        maxf = freq[25]
        idle = (maxf - 1) * n

        for i in range(0, 25):
            idle -= min(maxf - 1, freq[i])

        return max(0, idle) + len(tasks)
        