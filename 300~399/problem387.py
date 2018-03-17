# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = dict()
        for item in s:
            if item not in s_dict:
                s_dict[item] = 1
            else:
                s_dict[item] += 1

        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
        return -1

if __name__ == '__main__':
    print Solution().firstUniqChar("loveleetcodevtcd")