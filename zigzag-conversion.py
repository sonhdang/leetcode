# https://leetcode.com/problems/zigzag-conversion/

def convert(s, numRows):
    i = 0
    sign = True
    result = [''] * numRows
    while(s != ''):
        if sign:
            if i < numRows - 1:
                result[i] += s[0]
                i += 1
            else:
                result[i] += s[0]
                sign = False
                i -= 1
        else:
            if i > 0:
                result[i] += s[0]
                i -= 1
            else:
                result[i] += s[0]
                sign = True
                i += 1
        s = s[1:]

    return ''.join(result)