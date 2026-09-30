class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        last=0
        rev=0
        if x<0:
            x=-x
            while x>0:
                last=x%10
                rev=rev*10+last
                x=x//10
            rev=-rev
            if -2**31<=rev<=2**31-1:
                return rev
            else:
                return 0
        elif x>0:
            while x>0:
                last=x%10
                rev=rev*10+last
                x=x//10
            if -2**31<=rev<=2**31-1:
                return rev
            else:
                return 0
        else:
            return 0
