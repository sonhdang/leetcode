# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
#         Psedocode
#         [[ 4, 3, 2,-1],
#          [ 3, 2, 1,-1],
#          [ 1, 1,-1,-2],
#          [-1,-1,-2,-3]]
        
#         Checking every row from left to right, from bottom to the top
#             within a row, stop checking when you find a negative number
#             subtract the index from the row's length for number of negative numbers
#             decrement the row
#             start checking the index of where we stopped on the last row instead of 
#             from the beginning of the row
        
        totalNegatives = 0
        divider = 2
        m = len(grid)
        n = len(grid[0])
        i = 0
        pivot = 0
        for i in range(m - 1, -1, -1):
            while pivot < n:
                print(pivot)
                if grid[i][pivot] < 0:
                    totalNegatives += n - pivot
                    break
                else:
                    pivot += 1
        return totalNegatives