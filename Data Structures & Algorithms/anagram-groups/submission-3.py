class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for str in strs:
            letter = 26 * [0]
            for char in str:
                letter[ord(char) - ord("a")] += 1
            
            result[tuple(letter)].append(str)

        print(result.values())
        return list(result.values())