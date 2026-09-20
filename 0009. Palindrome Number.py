class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        nums=x
        rev=0
        while x>0:
            last=x%10
            rev=10*rev+last
            x=x//10
        if nums==rev:
            return True
        else:
            return False
