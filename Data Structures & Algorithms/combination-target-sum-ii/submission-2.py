class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solution 1: Recurive function that gets every forward combination
        res = []
        current = []
        candidates.sort()

        def getToTarget(start: int, target: int):
            if target == 0: # Target hit, add to res
                res.append(current[:])
                return
            if target < 0: # Target missed, return
                return
            for i in range(start, len(candidates)): # Only allow looking forward
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                getToTarget(i + 1, target - candidates[i]) # Only allow looking forward, no
                                                           # repeats
                current.pop()
            return
        
        getToTarget(0, target)
        return res