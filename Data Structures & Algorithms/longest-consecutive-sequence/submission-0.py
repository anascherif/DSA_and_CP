class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        i=0 
        l=0
        while (i<len(nums)):
            if nums[i]-1 not in n:
                base=nums[i]
                k=[base]
                while base+1 in n:
                    base=base+1
                    k.append(base)
                l=max(l,len(k))
            i+=1
        return l