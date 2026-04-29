class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # Check if substring is a palindrome
        def checkPalindrome(s: str) -> bool:
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        current = []
        res = []
        
        def recursion(k: int):
            if k == len(s):
                res.append(current[:])
                return
            for i in range(k, len(s)):
                sub2 = s[k:i + 1]
                if checkPalindrome(sub2):
                    current.append(sub2)
                    recursion(i + 1)
                    current.pop()
            return
        
        recursion(0)

        return res