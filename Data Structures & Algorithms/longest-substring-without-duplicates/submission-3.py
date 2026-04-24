class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       

        string = set()
        l = 0
        max_len = 0

        for i in range(len(s)):
            print(f"current char: {s[i]}")
            print(f"string set before: {string}")

            # Continuously remove all the duplicates
            while s[i] in string:
                string.remove(s[l])
                l += 1
            
            string.add(s[i])
            max_len = max(max_len, i - l + 1)
            print(f"string set after: {string}")
        
        return max_len
                
            




