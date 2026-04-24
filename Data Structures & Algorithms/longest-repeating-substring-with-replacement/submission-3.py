class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Having a dict to store most frqueent
        dict = {}
        result = 0
        maxFrequent = 0
        left = 0
        for r in range(len(s)):
            # For current alphabet, take notes in dict
            dict[s[r]] = dict.get(s[r], 0) + 1
            maxFrequent = max(maxFrequent, dict[s[r]])
            

            # Keep expanding the current window as long as
            # window length - most frequent alphabet not more than k
            while (r - left + 1) - maxFrequent > k:
                dict[s[left]] -= 1
                left += 1

            result = max(result, r - left + 1)


        return result 
            