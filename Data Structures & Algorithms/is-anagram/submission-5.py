class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sSort = sorted(s)
        tSort = sorted(t)

        if (sSort == tSort): return True
        else: return False