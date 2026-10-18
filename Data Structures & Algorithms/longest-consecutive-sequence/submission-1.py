class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
         
        l=0
        for num in n:
            if num-1 not in n:
                base=num
                k=1
                while base+1 in n:
                    base+=1
                    k+=1
                l=max(l,k)
            
        return l