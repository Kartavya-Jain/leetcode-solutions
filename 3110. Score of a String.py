class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=1
        sum=0
        while r<len(s) and 97<=ord(s[l])<=122:
            val=abs(ord(s[l])-ord(s[r]))
            sum+=val
            l+=1
            r+=1
        return sum