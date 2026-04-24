class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        result = []
        
        for left in range(len(s)):
            #Move the left pointer until found the first char that is in "t" 
            if s[left] not in dict_t:
                continue
            
            dict_s = {}
            # Track how many required characters (including counts) we have satisfied
            formed = 0
            required = len(dict_t)
            
            for right in range(left, len(s)):
                char = s[right]
                if char in dict_t:
                    dict_s[char] = dict_s.get(char, 0) + 1
                    if dict_s[char] == dict_t[char]:
                        formed += 1
                
                if formed == required:
                    temporary = list(s[left:right+1])
                    if len(result) == 0 or len(temporary) < len(result):
                        result = temporary
                    break

        return "".join(result)