# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        init_str = strs[0]
        for i in range(1, len(strs)):
            com_str = strs[i]
            if len(init_str)>len(com_str):
                init_str = init_str[:len(com_str)]
            for j in range(min(len(init_str), len(com_str))):
                if init_str[j] != com_str[j]:
                    init_str = init_str[0:j]
                    break

        return init_str

if __name__ == '__main__':
    print Solution().longestCommonPrefix(['lle', 'lle', 'llee'])
