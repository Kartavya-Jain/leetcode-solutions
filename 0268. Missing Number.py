class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        sum=0
        total=0
        while i<len(nums):
            sum=sum+nums[i]
            i+=1
        total=len(nums)*(len(nums)+1)//2
        return total-sum
