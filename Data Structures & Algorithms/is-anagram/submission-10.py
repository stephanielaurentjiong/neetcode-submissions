class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = Counter(s), Counter(t)
        if len(dictS) != len(dictT):
            return False

        for key, value in dictS.items():
            if dictT.get(key, 0) != value:
                return False

        return True

