# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p_dict = dict()
        count = 1
        p_list = []
        for item in pattern:
            if item not in p_dict:
                p_dict[item] = count
                p_list.append(count)
                count += 1
            else:
                p_list.append(p_dict[item])

        s_dict = dict()
        count = 1
        s_list = []
        for item in str.split(' '):
            if item not in s_dict:
                s_dict[item] = count
                s_list.append(count)
                count += 1
            else:
                s_list.append(s_dict[item])
        return p_list == s_list

if __name__ == '__main__':
    print Solution().wordPattern("abba", "dog cat cat fish")
