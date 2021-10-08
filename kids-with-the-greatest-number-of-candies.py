# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies, extraCandies):
    # O(n)
    # find the maximum of the array candies - maxCandy
    # iterate through each element
    #   if the ith + extracandies >= maxCandy
    #       append to the result list true
    #   else
    #       append to the result list false
    
    result = []
    maxCandy = max(candies)
    for i in candies:
        if extraCandies + i >= maxCandy:
            result.append(True)
        else:
            result.append(False)
    return result