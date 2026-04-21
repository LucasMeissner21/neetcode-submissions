class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check that the same number of letters for s and t
        if len(s) != len(t):
            return False
        # Initializing a dictionary (hashtable) for each word
        countS = {}
        countT = {}
        # Iterating through s and t, adding new letters to dictionary, updating duplicates
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # Checking if letter counts match up, returns False otherwise
        for letter in countS:
            if countS[letter] != countT.get(letter, 0):
                return False
        return True
