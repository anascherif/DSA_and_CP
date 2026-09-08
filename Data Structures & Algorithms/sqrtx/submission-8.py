class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        res = 0
        
        while i <= j:
            mid = (i + j) // 2
            
            if mid * mid <= x:
                res = mid     
                i = mid + 1   
            else:
                j = mid - 1    
                
        return res