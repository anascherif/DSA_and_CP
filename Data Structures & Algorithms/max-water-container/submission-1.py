class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r,l=0,len(heights)-1
        res=0
        while(r<l):
            sur=(l-r)*min(heights[l],heights[r])
            res=max(res,sur)
            if heights[r]<heights[l]:
                r+=1
            else:
                l-=1
        return res
        