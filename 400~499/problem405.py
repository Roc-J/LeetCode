# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # string = ''
        # number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
        # if num < 0:
        #     num += 0x100000000
        # while num > 15:
        #     r = num % 16
        #     num = num/16
        #     string = str(number[r]) + string
        # string = str(number[num]) + string
        # return string
        ans = []
        hexs = '0123456789abcdef'
        if num < 0:
            num += 0x100000000
        while num:
            ans.append(hexs[num % 16])
            num /= 16
        return ''.join(ans[::-1]) if ans else '0'


if __name__ == '__main__':
    print Solution().toHex(-260)