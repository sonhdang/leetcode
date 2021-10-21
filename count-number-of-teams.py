# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        # FIRST ATTEMPT: BRUTE FORCE
        # Pseudocode
        # starting from left to right, check for all the combinations
        # if the two soldier has increasing ranking, look for the third
        # if the two soldier has decreasing ranking, look for the third
        # totalTeam = 0
        # i = 0
        # while i < len(rating) - 2:
        #     j = i + 1
        #     while j < len(rating) - 1:
        #         k = j + 1
        #         if rating[i] < rating[j]:
        #             while k < len(rating):
        #                 if rating[j] < rating[k]:
        #                     totalTeam += 1
        #                 k += 1
        #         else:
        #             while k < len(rating):
        #                 if rating[j] > rating[k]:
        #                     totalTeam += 1
        #                 k += 1
        #         j += 1
        #     i += 1
        # return totalTeam
    
        # SECOND ATTEMPT: DYNAMIC PROGRAMMING
        # Pseodocode
        # Increasing order
        # create an array that stores the number of element the element at index
        # i is greater than
        # For example:
        # [2,5,3,4,1]
        # [1,3,1,1,0] Greater than
        # [3,0,1,0,0] Less than
        
        # creating greater than and less than arrays
        totalTeams = 0
        greater = [0 for _ in range(len(rating))]
        less = [0 for _ in range(len(rating))]
        i = 0
        while i < len(rating) - 1:
            j = i + 1
            while j < len(rating):
                if rating[i] > rating[j]:
                    greater[i] += 1
                else:
                    less[i] += 1
                j += 1
            i += 1
        
        # counting teams
        i = 0
        while i < len(rating) - 2:
            j = i + 1
            while j < len(rating) - 1:
                if rating[i] < rating[j]:   # Increasing
                    totalTeams += less[j]
                else:                       # Decreasing
                    totalTeams += greater[j]
                j += 1
            i += 1
        return totalTeams                    