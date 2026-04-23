class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c.isdigit():
                stack.append(int(c))
            elif c[0] == '-' and len(c) > 1:
                stack.append(-1 * int(c[1:]))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                match c:
                    case '+':
                        res = op2 + op1
                        stack.append(res)
                    case '-':
                        res = op2 - op1
                        stack.append(res)
                    case '*':
                        res = op2 * op1
                        stack.append(int(res))
                    case '/':
                        res = op2 / op1
                        stack.append(int(res))
        res = stack.pop()
        return int(res)
            