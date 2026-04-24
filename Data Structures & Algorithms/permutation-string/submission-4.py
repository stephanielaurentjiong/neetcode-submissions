from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if length of permutation is shorter
        if len(s1) > len(s2):
            return False

        # List of 26 elements. All zeros.
        # For s1 and s2 
        s1Count, s2Count = [0] * 26, [0] * 26
        

        # Make a dictionary for a window size of length s1
        for i in range(len(s1)):
        # Loop over the length of s1
            # Put the current character from s1
            # into s1Dict
            # Similarly for s2
            s1Count[ord(s1[i]) - ord('a')] += 1 
            # if s1Count[0] (example for a), 
            # Then at that index position, the element is 1
            # s2Count[ord(s2[i]) - ord('a')] += 1 
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # Find matches from the s1 and s2 dictionary for all the 26 index spots
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            # Check if all 26 position matches permutation
            if matches == 26:
                return True
            
            # Get the next character from s2 (expand right window)
            # Update the dictionary for s2 ONLY
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # Check matches s1 and s2 dictionary
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Check matches s1 and s2 dictionary
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1
            
            l += 1
        
        return matches == 26

        