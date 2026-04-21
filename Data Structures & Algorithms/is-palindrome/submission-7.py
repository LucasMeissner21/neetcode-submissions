class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Get rid of whitespace and lowercase all characters
        s = s.strip()
        s = s.lower()

        # Initialize 2-pointers
        i = 0
        j = len(s) - 1

        # Move pointers towards the middle, skipping over non-alphanumeric characters
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # If values are not equal, not palindrome
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True