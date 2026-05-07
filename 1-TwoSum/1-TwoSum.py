# Last updated: 5/8/2026, 3:50:17 AM
class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return([i,j])
                    