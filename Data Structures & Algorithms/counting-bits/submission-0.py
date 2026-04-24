class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(self.countOnes(i))
    
        return result

    
    def countOnes(self, n: int) -> int:
        counter = 0
        while n:
            n &= (n - 1)
            counter += 1
        
        return counter