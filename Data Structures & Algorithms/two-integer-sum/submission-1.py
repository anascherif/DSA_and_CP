class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see={}
        for i,n in enumerate(nums):
            if (target-n) in see:
                return [see[target-n],i]
            see[n]=i

        