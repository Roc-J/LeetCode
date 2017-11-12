# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = dict()
        for item in s:
            if item not in s_dict:
                s_dict[item] = 1
            else:
                s_dict[item] += 1
        t_dict = dict()
        for item in t:
            if item not in t_dict:
                t_dict[item] = 1
            else:
                t_dict[item] += 1
        return s_dict == t_dict