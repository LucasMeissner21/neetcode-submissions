class Solution:
    def isValid(self, s: str) -> bool:
        # Odd number of brackets will never be valid
        if len(s) % 2 != 0:
            return False
        # Mapping open to close brackets
        brackets = {'(' : ')', '[' : ']', '{' : '}'}

        stack = []
        for c in s:
            # If open bracket, append
            if brackets.get(c, 0) != 0:
                stack.append(c)
            # If close bracket and stack empty or non-matching bracket, return false
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if brackets.get(curr, 0) != c:
                    return False
        
        # Only valid if stack is empty
        return True if len(stack) == 0 else False