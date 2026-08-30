class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        i=0
        while i<len(nums):
            nums[i]=sum+nums[i]
            sum=nums[i]
            i+=1
        return nums
