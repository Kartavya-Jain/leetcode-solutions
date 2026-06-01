class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if 0<=haystack.find(needle)<=len(haystack):
               return haystack.index(needle)
        else:
             return -1