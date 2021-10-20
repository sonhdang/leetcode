# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

def sumZero(n):
    result = []
    for i in range(1, int(n/2) + 1):
        result.append(i)
        result.append(-i)
    if n % 2 != 0:
        result.append(0)
    return result