# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numberOfSteps(num):
        stepNum = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            stepNum += 1
        return stepNum