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

        l = 0
        for r in range(len(s1), len(s2)):
            if count1 == count2:
                return True

            index = ord(s2[r]) - ord('a')
            count2[index] += 1

            index = ord(s2[l]) - ord('a')
            count2[index] -= 1

            l += 1
        return count1 == count2