class Solution:
    def hammingWeight(self, n: int) -> int:
        
        number = 0
        
        for i in range(32):
            number += (n & 1)
            n = n >> 1
            
        return number
