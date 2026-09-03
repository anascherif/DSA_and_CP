class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        iii=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                iii.remove(nums[l])
                l+=1
            if(nums[r] in iii):
                return True
            iii.add(nums[r])
        return False