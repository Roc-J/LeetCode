# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        number1 = bin(n).replace('0b', '')
        if len(number1) < 32:
            number1 = '0' * (32-len(number1)) + number1
        number2 = ''
        for item in number1[::-1]:
            number2 += item
        return int(number2, 2)

if __name__ == '__main__':
    print Solution().reverseBits(43261596)
