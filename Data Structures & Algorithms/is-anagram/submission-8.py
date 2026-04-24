class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Direct check if two strings length is diff
        if (len(s) != len(t)): return False

        #Initalize a dictionary/hashmap
        hashmap = {}

        # Loop over the str
        for char in s:
            # If the char in hashmap, +1 to the value
            if char in hashmap:
                hashmap[char] += 1
            else: #Otherwise, create new key value pair
                hashmap[char] = 1
        
       
        # For each char in t, decrease the value in hashmap
        for char in t:
            if char not in hashmap or hashmap[char] == 0:
                return False        
            else:
                hashmap[char] -= 1
        
        return True