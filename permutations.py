# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        def permuteRecursive(prefix, postfix):
            # Base case
            if len(postfix) <= 1:
                return [prefix + postfix]
            
            # Recursion
            result = []
            for i in range(len(postfix)):
                # Swap
                copy = postfix
                temp = postfix[0]
                postfix[0] = postfix[i]
                postfix[i] = temp
                
                # Recursive Call
                result += (permuteRecursive(prefix + [postfix[0]], postfix[1:]))
                
                # Backtrack
                postfix = copy
            return result
        
        result = permuteRecursive([], nums)
        return result