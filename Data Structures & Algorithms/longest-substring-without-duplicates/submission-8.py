class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        left = 0
        maxSubstring = 0
      

        for r in range(len(s)):
            while s[r] in string:  
                string.remove(s[left]) 
                left += 1

            string.add(s[r])
            maxSubstring = max(maxSubstring, r - left + 1)
            
        return maxSubstring






