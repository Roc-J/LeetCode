# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            idx = haystack.index(needle)
        except:
            idx = -1
        return idx

if __name__ == '__main__':
    print Solution().strStr('', '')
