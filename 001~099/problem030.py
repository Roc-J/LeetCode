#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

from collections import Counter, defaultdict
class Solution(object):
    def test(self, sub_str, word_len, ctr):
        i, seen = 0, defaultdict(int)
        while i < len(sub_str):
            next_word = sub_str[i:i + word_len]
            if next_word not in ctr or seen[next_word] == ctr[next_word]:
                return False
            seen[next_word], i = seen[next_word] + 1, i + word_len
        return True

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        start, end, result = 0, len(words) * len(words[0]) - 1, []
        ctr = Counter(words)
        while end < len(s):
            if self.test(s[start:end + 1], len(words[0]), ctr):
                result.append(start)
            start, end = start + 1, end + 1
        return result
        # indexs = []
        # result = []
        # t = 0
        # flag = 0
        # while True:
        #     indexs = []
        #     for item in words:
        #         if item not in s[t:]:
        #             flag = 1
        #             break
        #         indexs.append(s[t:].index(item))
        #     print(indexs)
        #     if flag == 1:
        #         break
        #     if (max(indexs) - min(indexs)) == len(words[0])*(len(indexs)-1):
        #         if t+min(indexs) not in result:
        #             result.append(t+min(indexs))
        #     t = t+len(words[0])
        #
        # return result

        # result = []
        # length = len("".join(words))
        # idx = len(words[0])
        # for i in range(len(s)-length+1):
        #     refenrence = words[:]
        #     substr = s[i:i+length]
        #     while True:
        #         item = substr[:idx]
        #         if item not in refenrence:
        #             break
        #         refenrence.remove(item)
        #         substr = substr[idx:]
        #         if len(refenrence) == 0:
        #             result.append(i)
        #             break
        # return result

        # '''
        # 遍历方式采用两张
        # 第一种是按照单词的长度从头遍历
        # 第二次遍历单词的一个长度来进行
        #
        # '''
        # if len(s) == 0 or len(words) == 0 or len(words[0]) == 0:
        #     return []
        #
        # L = {}
        # for word in words:
        #     L[word] = 1 if word not in L else L[word] + 1
        #
        # l = len(words[0])
        # ret = []
        # for i in range(0, l):
        #     b = i
        #     curr = {}
        #     for j in xrange(b, len(s), l):
        #         word = s[j:j+l]
        #         if word in L:
        #             if word not in curr:
        #                 curr[word] = 1
        #             elif curr[word] < L[word]:
        #                 curr[word] += 1
        #             else:
        #                 while s[b:b+l] != word:
        #                     b += l
        #                     curr[s[b:b+l]] -= 1
        #                     if curr[s[b:b+l]] == 0:
        #                         del curr[s[b:b+l]]
        #                 b += l
        #         else:
        #             curr = {}
        #             b = j + l
        #
        #
        #         if sum(curr.values()) == len(words):
        #             print(curr)
        #             ret.append(b)
        #             curr[s[b:b+l]] -= 1
        #             if curr[s[b:b+l]] == 0:
        #                 del curr[s[b:b+l]]
        #             b += l
        #
        # return ret

if __name__ == '__main__':
    print(Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))