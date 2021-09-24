# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        maxstr = ""
        i = 0
        while maxlen < len(s):
            c_str = ""
            c_len = 0
            for c in s:
                if c not in c_str:
                    c_len += 1
                    c_str += c
                else:
                    s = s[1:]
                    break
            if c_len > maxlen:
                maxstr = c_str
                maxlen = c_len
        return maxlen
                