class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        # Map all digit inputs to their potential characters
        numToChar = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
                    "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        # Recursive call
        def recursion(k: int):
            # Return when all input digits present in curr
            if k == len(digits):
                res.append("".join(curr))
                return

            # Check every possible character for current digit and recursive call
            for j in range(len(numToChar[digits[k]])):
                curr.append(numToChar[digits[k]][j])
                recursion(k + 1) # Advance to next digit
                curr.pop()

            return

        curr = []
        res = []

        recursion(0)
        return res