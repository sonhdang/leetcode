# https://leetcode.com/problems/reverse-integer/

def reverse(x):
    li = list(str(x))
    if x < 0:
        s = ''.join(['-'] + li[len(li):0:-1])
        reverse = int(s)
    else:
        li.reverse()
        reverse = int(''.join(li))
    if reverse not in range(-2**31, 2**31):
        return 0
    else:
        return reverse