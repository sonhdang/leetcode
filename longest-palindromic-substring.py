def longestPalindrome(s):
    if len(s) == 1:
        return s
    elif len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    else:
        case1 = longestPalindrome(s[1:len(s)-1])
        case2 = longestPalindrome(s[0:len(s)-1])
        case3 = longestPalindrome(s[1:])

    print(case1)
    print(case2)
    print(case3)
    print()
    
    if s[0] == s[-1] and (len(case1) == len(s) - 2 or len(case2) == len(s) - 1 or len(case3) == len(s) - 1):
            return s
    else:
        if len(case2) >= len(case3) and len(case2) >= len(case1):
            return case2
        elif len(case3) >= len(case2) and len(case3) >= len(case1):
            return case3
        else:
            return case1

print(longestPalindrome("abbcccbbbcaaccbababcbcabca"))
