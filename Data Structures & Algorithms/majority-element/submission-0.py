class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max=0
        i=0
        l=0
        while i<len(nums):
            if (nums.count(nums[i]))>=max:
                max=nums.count(nums[i])
                l=nums[i]
            i+=1
        return l