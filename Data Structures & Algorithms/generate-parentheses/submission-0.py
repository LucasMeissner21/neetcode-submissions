class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking
        res = []
        current = ["("]
        remain = {"(" : n - 1, ")" : n}

        def getResults():
            if len(current) == 2 * n:
                res.append("".join(current))
                return

            if remain["("] > 0:
                current.append("(")
                remain["("] -= 1
                getResults()
                current.pop()
                remain["("] += 1
            if remain[")"] > remain["("]:
                current.append(")")
                remain[")"] -= 1
                getResults()
                current.pop()
                remain[")"] += 1

            return
        

        getResults()
        return res