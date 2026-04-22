class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case, no permutations possible
        if len(s1) > len(s2):
            return False

        # Initialize count array for perm string and sliding window (size 26 for 26 letters possible)
        count1 = [0] * 26
        count2 = [0] * 26

        # Check first len(s1) characters in s1 and s2 and adjust counts
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Get initial matches for initial window
        countM = 0
        for i in range(26):
            if count1[i] == count2[i]:
                countM += 1
        
        # Now use sliding window and update counts for right being added and left being removed each time,
        # Then adjust matches accordingly
        l = 0
        for r in range(len(s1), len(s2)):
            if countM == 26:
                return True

            index = ord(s2[r]) - ord('a')
            count2[index] += 1

            if count1[index] == count2[index]:
                countM += 1
            elif count1[index] + 1 == count2[index]: # Plus 1 to only update if new r removes a previous match
                countM -= 1

            index = ord(s2[l]) - ord('a')
            count2[index] -= 1

            if count1[index] == count2[index]:
                countM += 1
            elif count1[index] - 1 == count2[index]: # Minus 1 to only update if new l removes a previous match
                countM -= 1

            l += 1
        return countM == 26