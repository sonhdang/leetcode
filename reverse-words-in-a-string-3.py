# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        reversedWords = list(map(lambda x : x[::-1], li))
        result = ' '.join(reversedWords)
        return result