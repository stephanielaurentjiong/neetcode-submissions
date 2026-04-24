class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # string = set()
        # left = 0
        # maxSubstring = 0
      

        # for r in range(len(s)):
        #     while s[r] in string:  
        #         string.remove(s[left]) 
        #         left += 1

        #     string.add(s[r])
        #     maxSubstring = max(maxSubstring, r - left + 1)
            
        # return maxSubstring

        max_length = 0
        curr_length = 0
        unique_words = deque()

        for char in s:
            while char in unique_words:
                unique_words.popleft()
                curr_length -= 1

            unique_words.append(char)
            curr_length += 1
            max_length = max(max_length, curr_length)

        return max_length





