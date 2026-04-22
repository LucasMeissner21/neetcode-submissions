class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        brackets = {'(' : ')', '[' : ']', '{' : '}'}

        stack = []
        for c in s:
            if brackets.get(c, 0) != 0:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if brackets.get(curr, 0) != c:
                    return False
        
        return True if len(stack) == 0 else False