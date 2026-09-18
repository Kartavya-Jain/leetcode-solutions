class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=0
        while x<32:
            if n==4**x:
                return True
            else:
                x+=1
        return False
