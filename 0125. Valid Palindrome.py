class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=""
        i=0
        s=s.lower()
        while i<len(s):
                if s[i].isalnum()==True:
                    res=res+s[i]
                    i+=1
                else:
                    i+=1
        rev=res[::-1]
        if res==rev:
            return True
        else:
            return False
