class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution 3: Use math relationship, result will be max of length of tasks and 
        # time required to complete task with highest frequency

        # Get frequencies
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # Get max frequency
        maxf = max(freq)
        maxCount = 0

        # Count how many tasks have maxf frequency
        for i in freq:
            maxCount += 1 if i == maxf else 0

        # Calculate ammount of time to complete with idle time based on maxf
        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
        