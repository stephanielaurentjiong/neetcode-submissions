class Solution:
    def climbStairs(self, n: int) -> int:
        #Initalize var:
            #one = 1
            #two = 1
        one, two = 1, 1

        #Loop over the n-1 elements
        for i in range(n-1):
            #Set one to the n-2's element
            #Set two two the n-1's element
            #Then shift both
            temp = one
            one = one + two
            two = temp
        
        return one