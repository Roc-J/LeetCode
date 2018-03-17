# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        strs = s.strip().split(' ')
        return len(strs[len(strs)-1])

if __name__ == '__main__':
    print Solution().lengthOfLastWord('a  ')