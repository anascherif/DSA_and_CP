class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = [0]*26
        for i in range(len(s)):
            l[ord(s[i]) - ord("a")] += 1
            
        for i in range(len(t)):
            l[ord(t[i]) - ord("a")] -= 1
    
        for v in l:
            if v!=0:
                return False
                
        return True