# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dict = dict()
        s_list = ''
        count = 0
        for item in s:
            if item not in s_dict:
                s_dict[item] = count
                s_list += str(count)
                count += 1
            else:
                s_list += str(s_dict[item])

        t_dict = dict()
        t_list = ''
        count = 0
        for item in t:
            if item not in t_dict:
                t_dict[item] = count
                t_list += str(count)
                count += 1
            else:
                t_list += str(t_dict[item])

        if s_list == t_list:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isIsomorphic("foro", "baca")