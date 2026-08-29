class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.upper()
        i=0
        j=len(s)-1
        ok=True
        while (i<j and ok):
            while i<j and not (s[i].isalnum()):
                i+=1
            while i<j and not (s[j].isalnum()):
                j-=1
                   
            if s[i]!=s[j]:
                ok=False
            i+=1
            j-=1
        return ok 


