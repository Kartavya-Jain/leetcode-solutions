import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num=math.sqrt(num)
        if num==int(num):
            return True
        else:
            return False
        
