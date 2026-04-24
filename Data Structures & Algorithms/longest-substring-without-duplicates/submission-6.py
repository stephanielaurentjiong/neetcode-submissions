class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        string = set()
        longest = 0
        left = 0

    
        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[left])
                left += 1
            string.add(s[r])
            longest = max(longest, r - left + 1) 
        return longest



