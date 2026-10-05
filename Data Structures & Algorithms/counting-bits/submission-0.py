class Solution:
    def countBits(self, n: int) -> List[int]:
        h=[]
        for i in range(n+1):
            h.append(bin(i).count('1'))
        return h 