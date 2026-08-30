class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(k,m):
            while k<m:
                if s[k]!=s[m]:
                    return False
                k+=1
                m-=1
            return True 
        
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return (ispalindrome(i+1,j) or ispalindrome(i,j-1))
            
            i += 1
            j -= 1
            
        return True