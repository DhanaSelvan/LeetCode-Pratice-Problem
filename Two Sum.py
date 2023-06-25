class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                Sum = nums[i] + nums[j]
                if(Sum == target):
                    return [i,j]
