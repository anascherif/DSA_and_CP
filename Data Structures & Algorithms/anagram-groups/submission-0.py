class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k={}
        for mot in strs :
            r=[0]*26
            for j in range(len(mot)) :
                r[ord(mot[j])-ord("a")]+=1
            k.setdefault(tuple(r), []).append(mot)

        return list(k.values())