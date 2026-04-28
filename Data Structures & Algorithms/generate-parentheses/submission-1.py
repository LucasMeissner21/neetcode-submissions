class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking through solutions
        res = []
        current = ["("]
        remain = {"(" : n - 1, ")" : n}

        def getResults():
            # Basecase, add result if length matches
            if len(current) == 2 * n:
                res.append("".join(current))
                return

            # Only add open parenthesis if there are some to add
            if remain["("] > 0:
                current.append("(")
                remain["("] -= 1
                getResults()
                current.pop()
                remain["("] += 1
            # Only add closed parenthesis if there are more of them than open
            if remain[")"] > remain["("]:
                current.append(")")
                remain[")"] -= 1
                getResults()
                current.pop()
                remain[")"] += 1
            return
        

        getResults()
        return res